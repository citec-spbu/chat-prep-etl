package main

import (
	"encoding/json"
	"net/http"
	"net/url"
	"os"
	"testing"
	"time"
)

func getBaseURL() string {
	url := os.Getenv("ETL_PORT")
	if url == "" {
		return "http://localhost:8067"
	}
	return url
}

var baseURL = getBaseURL()

type HealthResponse struct {
	Status     string `json:"status"`
	Components struct {
		EtlService string `json:"etl_service"`
		Qdrant     string `json:"qdrant"`
	} `json:"components"`
}

type SearchResponse struct {
	Results []interface{} `json:"results"`
	Detail  string        `json:"detail,omitempty"`
}

func TestLive_HealthCheck(t *testing.T) {
	client := &http.Client{Timeout: 5 * time.Second}

	resp, err := client.Get(baseURL + "/health/")
	if err != nil {
		t.Fatalf("API недоступно по адресу %s. Ошибка: %v", baseURL, err)
	}
	defer resp.Body.Close()
	if resp.StatusCode == http.StatusServiceUnavailable {
		t.Log("WARNING: Сервис запущен, но БД недоступна (503 Service Unavailable)")
		return
	}

	if resp.StatusCode != http.StatusOK {
		t.Fatalf("Ожидали статус 200 OK, получили: %d", resp.StatusCode)
	}

	var health HealthResponse
	if err := json.NewDecoder(resp.Body).Decode(&health); err != nil {
		t.Fatalf("Не удалось распарсить JSON ответа: %v", err)
	}

	if health.Status != "healthy" || health.Components.EtlService != "up" {
		t.Errorf("Неожиданное состояние системы: %+v", health)
	}

	t.Logf("Успешно! Статус системы: %s (Qdrant: %s)", health.Status, health.Components.Qdrant)
}

func TestLive_Search_Success(t *testing.T) {
	client := &http.Client{Timeout: 5 * time.Second}

	params := url.Values{}
	params.Add("query", "67676767")
	params.Add("chat_id", "101")
	params.Add("k", "1")
	params.Add("clean", "raw")

	searchURL := baseURL + "/search?" + params.Encode()

	resp, err := client.Get(searchURL)
	if err != nil {
		t.Fatalf("Ошибка отправки запроса поиска: %v", err)
	}
	defer resp.Body.Close()
	if resp.StatusCode != http.StatusOK {
		t.Fatalf("Поиск вернул ошибку, статус: %d. ", resp.StatusCode)
	}

	var searchResp SearchResponse
	if err := json.NewDecoder(resp.Body).Decode(&searchResp); err != nil {
		t.Fatalf("Ошибка декодирования JSON поиска: %v", err)
	}

	t.Logf("Успешно! Получено результатов: %d", len(searchResp.Results))
}
func TestLive_Search_ValidationError_EmptyQuery(t *testing.T) {
	client := &http.Client{Timeout: 5 * time.Second}

	searchURL := baseURL + "/search?query=&chat_id=101&clean=raw"

	resp, err := client.Get(searchURL)
	if err != nil {
		t.Fatalf("Ошибка отправки: %v", err)
	}
	defer resp.Body.Close()
	if resp.StatusCode != http.StatusUnprocessableEntity {
		t.Errorf("Ожидали ошибку валидации 422 для пустого запроса, получили: %d", resp.StatusCode)
	}
}
