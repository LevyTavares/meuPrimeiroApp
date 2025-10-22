// Minimal HTTP client for the frontend to talk to the FastAPI backend

const DEFAULT_TIMEOUT_MS = 15000;

function getBaseUrl() {
  // Expo exposes public env vars via process.env.EXPO_PUBLIC_*
  const envUrl = process.env.EXPO_PUBLIC_API_URL;
  return envUrl && typeof envUrl === "string" && envUrl.length > 0
    ? envUrl
    : "http://localhost:8000";
}

async function request(
  path,
  { method = "GET", headers = {}, body, timeout = DEFAULT_TIMEOUT_MS } = {}
) {
  const controller = new AbortController();
  const id = setTimeout(() => controller.abort(), timeout);
  const url = `${getBaseUrl()}${path}`;
  try {
    const res = await fetch(url, {
      method,
      headers: { "Content-Type": "application/json", ...headers },
      body: body ? JSON.stringify(body) : undefined,
      signal: controller.signal,
    });
    if (!res.ok) {
      const text = await res.text().catch(() => "");
      throw new Error(`HTTP ${res.status} ${res.statusText} - ${text}`);
    }
    // try json, fallback text
    const ct = res.headers.get("content-type") || "";
    if (ct.includes("application/json")) return await res.json();
    return await res.text();
  } finally {
    clearTimeout(id);
  }
}

// API surface
export async function createGabarito({
  titulo,
  num_questoes,
  alternativas,
  respostas_corretas,
  descricao = null,
}) {
  return request("/api/gabaritos/", {
    method: "POST",
    body: { titulo, num_questoes, alternativas, respostas_corretas, descricao },
  });
}

export function getApiBaseUrl() {
  return getBaseUrl();
}

export default {
  createGabarito,
  getApiBaseUrl,
};
