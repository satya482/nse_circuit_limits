from discord_alert import send_discord_alert


def test_send_discord_alert_skips_without_webhook_env(monkeypatch):
    monkeypatch.delenv("DISCORD_WEBHOOK_URL", raising=False)

    assert send_discord_alert("title", "message") is False


def test_send_discord_alert_posts_embed_when_webhook_set(monkeypatch):
    monkeypatch.setenv("DISCORD_WEBHOOK_URL", "https://discord.example/webhook")
    captured = {}

    class FakeResponse:
        status_code = 204

    def fake_post(url, json, timeout):
        captured["url"] = url
        captured["json"] = json
        return FakeResponse()

    monkeypatch.setattr("discord_alert.requests.post", fake_post)

    assert send_discord_alert("Breadth Monitor", "breadth.html generated") is True
    assert captured["url"] == "https://discord.example/webhook"
    assert captured["json"]["embeds"][0]["title"] == "Breadth Monitor"
