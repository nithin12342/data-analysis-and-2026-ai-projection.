# AI Model & API Pricing Master List
*Extracted from "Directly Chat with Frontier AI Search Models" - Verified as of July 16, 2026*

---

## 📋 Table of Contents
1. [US-Based Inference Providers](#us-based-inference-providers)
2. [European Providers](#european-providers)
3. [Chinese Providers](#chinese-providers)
4. [Gateway/Proxy Tools](#gatewayproxy-tools)
5. [Major Model Families & Pricing](#major-model-families--pricing)
6. [Grand Comparison Summary](#grand-comparison-summary)

---

## 🇺🇸 US-Based Inference Providers

### 1. OpenRouter (API Aggregator)
- **Type**: API Aggregator / Unified Gateway
- **HQ**: San Francisco, USA
- **Fee**: 5.5% credit fee (non-crypto)
- **Models**: 300-500+
- **OpenAI Compatible**: ✅ Yes
- **Enterprise**: ✅ Negotiated SLA
- **BYOK**: ✅ Yes
- **Free Tier**: ✅ Free models available

| Category | Models |
|----------|--------|
| Meta | Llama 3.3 70B, Llama 4 Scout/Maverick |
| DeepSeek | V3, V4-Pro, R1, R1-0528 |
| Qwen | 3.5 Flash, 3.6 Plus, 3 (all sizes) |
| GLM | GLM-5.2, GLM-4.7-Flash |
| Kimi | K2.5, K2.6, K2.7 |
| MiniMax | M2.5, M2.7, M3 |
| Mistral | Mixtral, Mistral Large, Mistral Small |
| OpenAI | GPT-4o, GPT-5, o3 |
| Anthropic | Claude 3.5 Sonnet, Claude 4 |
| Google | Gemini 2.5 Flash, Gemini 3 Pro |
| MiMo | V2 Flash, V2 Pro |

### 2. Together AI (First-Party Inference + Research Lab)
- **Type**: First-Party Inference Provider + Research Lab
- **HQ**: San Francisco, USA
- **Hardware**: NVIDIA GB200, B200, H200
- **Models**: 200+ open-weight
- **Fine-tuning**: ✅ Yes (same platform)
- **SOC 2**: ✅ Type II
- **Free Credits**: ✅ On signup

| Model | Input /1M | Output /1M |
|-------|-----------|------------|
| Llama 4 Scout | $0.17 | $0.17 |
| Llama 3.3 70B | $0.50 | $0.70 |
| DeepSeek V4 Pro | $2.10 | $4.20 |
| Kimi K2.6 | $1.20 | $4.80 |
| Qwen 3.5 72B | $0.60 | $2.40 |
| Mistral 7B | $0.20 | $0.20 |
| Mixtral 8x22B | $1.20 | $1.20 |
| FLUX.1 Dev (image) | $0.025/img | — |
| Gemma 3 27B | $0.40 | $0.80 |

### 3. Fireworks AI (Speed Focused)
- **Type**: First-Party Inference Provider (Speed Focused)
- **HQ**: San Francisco, USA
- **Engine**: FireAttention (4x lower latency for structured output)
- **Models**: 202+
- **Fine-tuning**: ✅ Yes
- **SOC 2**: ✅ Type II
- **HIPAA**: ✅ Via BAA
- **Cached Input Discount**: ✅ 50% off
- **Free Credits**: ✅ $1 on signup

| Model | Input /1M | Output /1M | Cached |
|-------|-----------|------------|--------|
| Llama 3.3 70B | $0.90 | $0.90 | ✅ 50% off |
| Llama 4 Maverick | $0.40 | $1.60 | ✅ |
| DeepSeek V3 | $0.90 | $0.90 | ✅ |
| DeepSeek V4 Pro | $1.74 | $3.48 | ✅ |
| Qwen 3.5 72B | $0.60 | $2.40 | ✅ |
| Kimi K2.6 | $0.95 | $3.80 | ✅ |
| Mistral Large 3 | $2.00 | $6.00 | ✅ |
| GLM-5.2 | $1.40 | $5.60 | ✅ |
| SDXL (image) | $0.013/img | — | N/A |
| Gemma 3 9B | $0.10 | $0.10 | ✅ |
| **DeepSeek V4 Flash** | **$0.07** | **$0.14** | ✅ |

### 4. Groq (Custom LPU Hardware)
- **Type**: Custom Hardware Inference (LPU-Based)
- **HQ**: Mountain View, USA
- **Models**: 16
- **Speed**: ~476 tokens/sec (LPU)
- **TTFT**: 0.60-0.87 seconds
- **Free Tier**: ✅ 30 RPM, 14.4K req/day
- **Cached Discount**: ✅ 50% off
- **Fine-tuning**: ❌ No

| Model | Input /1M | Output /1M | Speed |
|-------|-----------|------------|-------|
| Llama 3.3 70B | $0.59 | $0.79 | ~476 tok/s |
| Llama 4 Scout | $0.11 | $0.34 | Ultra-fast |
| Qwen3 32B | $0.29 | $0.59 | Fast |
| DeepSeek R1 | $0.75 | $0.99 | Fast |
| Kimi K2 | $1.00 | $3.00 | Fast |
| GPT-OSS 20B | $0.15 | $0.60 | ~500+ tok/s |
| GPT-OSS 120B | $0.15 | $0.60 | ~476 tok/s |
| Mistral Nemo | $0.10 | $0.10 | Ultra-fast |
| Gemma 3 27B | $0.10 | $0.10 | Fast |

### 5. DeepInfra (Budget Leader)
- **Type**: First-Party Serverless Inference (Budget Leader)
- **HQ**: USA
- **Hardware**: H100 + A100 optimized
- **Models**: Widest catalog
- **Free Tier**: ❌ Postpaid, no minimum
- **Fine-tuning**: ❌ No
- **TTFT**: 0.49-0.77 seconds

| Model | Input /1M | Output /1M | Cached |
|-------|-----------|------------|--------|
| GPT-OSS 120B | $0.039 | $0.190 | N/A |
| DeepSeek V4 Pro | $1.30 | $2.60 | $0.10 |
| DeepSeek V4 Flash | $0.10 | $0.20 | N/A |
| Kimi K2.6 | $0.75 | $3.50 | N/A |
| Qwen 3.5 72B | $0.40 | $1.60 | N/A |
| GLM-5.2 | $1.18 | $4.14 | N/A |
| MiniMax-M2 | $0.20 | $0.80 | N/A |
| Llama 4 Scout | $0.17 | $0.17 | N/A |
| Llama 3.3 70B | $0.23 | $0.40 | N/A |
| NVIDIA Nemotron | $0.20 | $0.20 | N/A |

**Note**: DeepInfra prices DeepSeek V4 Pro cached input at **$0.10** (vs $1.30 uncached) — a **92% saving** for agent loops with large fixed system prompts.

**Additional Note**: DeepInfra also offers **DeepSeek-Chat (V2/V2.5)** at **$0.014/$0.028** per 1M tokens — the cheapest option from a frontier-capable provider.

### 6. Cerebras (WSE Ultra-Throughput)
- **Type**: Custom Hardware Inference (WSE-Based)
- **HQ**: Sunnyvale, USA
- **Models**: ~4 (narrow catalog)
- **Speed**: ~3,000 tokens/sec (highest measured)
- **Pricing Model**: Subscription tiers
- **Free Tier**: ✅ Free tier across all models
- **OpenAI Compatible**: ⚠️ Partial (drops some params)
- **Fine-tuning**: ❌ No

| Model | Pricing |
|-------|---------|
| GPT-OSS 120B | Subscription |
| GPT-OSS 20B | Subscription |
| Llama 3.3 70B | Subscription |
| DeepSeek R1 | Subscription |

**⚠️ Compatibility Gap**: Cerebras drops `frequency_penalty`, `logit_bias`, and `presence_penalty`, returning 400 error if supplied.

### 7. Replicate (Model Marketplace)
- **Type**: Open-Source Model Marketplace (Per-Prediction)
- **HQ**: San Francisco, USA
- **Models**: 100,000+
- **Pricing**: Per prediction / per second
- **OpenAI Compatible**: ❌ Own API format
- **Free Credits**: ✅ On signup

| Model | Price |
|-------|-------|
| FLUX Schnell (image) | $0.003/image |
| FLUX Dev (image) | $0.025/image |
| FLUX 1.1 Pro (image) | $0.04/image |
| GPU Time (H100) | $5.49/hr |
| GPU Time (A100 80GB) | $5.04/hr |

**⚠️ Cold Start Warning**: Non-warmed model cold starts average **18.4 seconds** across 500 popular models.

### 8. Modal (Serverless GPU Infrastructure)
- **Type**: Serverless GPU Infrastructure (Code-First)
- **HQ**: New York, USA
- **Pricing**: Per second (GPU time)
- **Cold Start**: <1 second
- **Free Credits**: ✅ $30/month on Starter
- **SOC 2**: ✅ Yes

| GPU Type | Price/hr |
|----------|----------|
| H100 | ~$3.95/hr |
| B200 | ~$6.25/hr |

### 9. Baseten (Enterprise Model Serving)
- **Type**: Enterprise Model Serving Platform
- **HQ**: San Francisco, USA
- **SOC 2**: ✅ Type II
- **HIPAA**: ✅ Yes

| GPU Type | Price/hr |
|----------|----------|
| H100 Dedicated | $6.50/hr |
| B200 | $9.98/hr |

### 10. Novita AI (Developer-First Cloud + API)
- **Type**: Developer-First GPU Cloud + Model API Hybrid
- **HQ**: USA
- **GPU Types**: H100, H200, RTX 5090
- **Models**: 200+
- **OpenAI Compatible**: ✅ Yes
- **vLLM Engine**: ✅ Partnership with vLLM

| Model | Input /1M | Output /1M |
|-------|-----------|------------|
| Kimi K2.6 | $0.80 | $3.20 |
| DeepSeek V4 Flash | $0.07 | $0.14 |
| Llama 4 Scout | $0.17 | $0.17 |
| Qwen 3.5 72B | $0.40 | $1.60 |
| **DeepSeek V4 Pro** | **$1.30** | **$2.60** |
| **GLM-5.2** | **$1.18** | **$4.14** |

### 11. Hugging Face (Model Hub + Inference)
- **Type**: Open-Source Model Hub + Managed Inference
- **HQ**: New York, USA
- **Models**: 2 million+
- **Inference Partners**: 18 (Fireworks, Together, Groq, Cerebras)
- **Markup**: Zero on provider rates
- **OpenAI Compatible**: ⚠️ Chat completions only

| Plan | Price |
|------|-------|
| Free | $0/month (limited) |
| Pro | $9/month |
| Enterprise Hub | $20+/user/month |
| Dedicated Inference Endpoints | From $0.06/hr (CPU) to $4.50/hr (A100) |

### 12. Featherless AI (Data Sovereignty Focused)
- **Type**: Open-Source Model Host (Data Sovereignty Focused)
- **HQ**: San Francisco, USA
- **Models**: 30,000+
- **Data Residency**: 🇺🇸 US-only servers
- **Pricing**: Per token
- **Focus**: Open-weight model access with data sovereignty

### 13. RunPod (GPU Cloud / Self-Deploy)
- **Type**: GPU Cloud / Self-Deploy Infrastructure
- **HQ**: USA
- **GPU Types**: H100, A100, RTX 4090, etc.
- **Pricing**: From $0.39/hr (RTX 3090) to $4.69/hr (H100)
- **OpenAI Compatible**: ✅ Via vLLM deployment
- **Spot Instances**: ✅ Yes (cheaper)
- **Persistent Storage**: ✅ Yes

### 14. AWS Bedrock (Enterprise Managed)
- **Type**: Enterprise Managed Inference (Multi-Model)
- **HQ**: Seattle, USA
- **Models Hosted**: 50+
- **Compliance**: SOC 2, HIPAA, FedRAMP
- **OpenAI Compatible**: ⚠️ Own Bedrock API
- **Fine-tuning**: ✅ Yes

| Model | Input /1M | Output /1M |
|-------|-----------|------------|
| Llama 4 Scout | $0.17 | $0.17 |
| Llama 3.3 70B | $0.72 | $0.72 |
| Mistral Large 2 | $3.00 | $9.00 |
| Mistral Small 3 | $0.10 | $0.30 |
| Qwen 2.5 72B | $0.50 | $1.50 |
| DeepSeek R1 | $1.35 | $5.40 |
| Gemma 3 9B | $0.10 | $0.10 |

### 15. Azure AI Foundry (Microsoft)
- **Type**: Enterprise Managed Inference (Multi-Model)
- **HQ**: Redmond, USA
- **Models Available**: 85
- **Compliance**: SOC 2, HIPAA, FedRAMP
- **OpenAI Compatible**: ✅ Yes
- **Fine-tuning**: ✅ Yes
- **Data Residency**: ✅ Multi-region

| Model | Input /1M | Output /1M |
|-------|-----------|------------|
| Llama 3.3 70B | $0.77 | $0.77 |
| Llama 4 Scout | $0.17 | $0.17 |
| Mistral Large 2 | $2.00 | $6.00 |
| Qwen 2.5 72B | $0.40 | $1.20 |
| DeepSeek R1 | $1.35 | $5.40 |
| Phi-4 | $0.07 | $0.14 |
| Phi-4 Mini | $0.07 | $0.23 |

### 16. Google Cloud Vertex AI
- **Type**: Enterprise Managed Inference
- **HQ**: Mountain View, USA
- **Models Available**: 150+ (Model Garden)
- **Compliance**: SOC 2, HIPAA, FedRAMP
- **Fine-tuning**: ✅ Yes

| Model | Pricing |
|-------|---------|
| Llama 3.3 70B | $0.77/1M input |
| Gemma 3 (all sizes) | $0.07-$0.60/1M |
| Mistral Large 2 | $2.00/1M input |
| DeepSeek R1 | $1.35/1M input |

---

## 🇪🇺 European Providers

### 17. Mistral AI (via la Plateforme) 🇫🇷
- **Type**: First-Party + Open-Weight Host
- **HQ**: Paris, France
- **OpenAI Compatible**: ✅ Yes (drop-in)
- **Enterprise**: ✅ Le Chat Enterprise
- **EU Data Residency**: ✅ Yes
- **Free Tier**: ✅ Limited

### 18. Aleph Alpha 🇩🇪
- **Type**: European Sovereign AI Inference
- **HQ**: Heidelberg, Germany
- **Data Residency**: 🇩🇪 Germany only
- **Enterprise**: ✅ Full enterprise
- **Compliance**: GDPR, EU AI Act ready
- **OpenAI Compatible**: ✅ Yes

### 19. Nebius AI 🇪🇺
- **Type**: European GPU Inference
- **HQ**: Amsterdam, Netherlands
- **Data Residency**: 🇪🇺 EU
- **OpenAI Compatible**: ✅ Yes
- **Enterprise**: ✅ Yes
- **Pricing**: Competitive per-token

### 20. AI Sweden / NVIDIA LAION 🇸🇪
- **Type**: EU Research + Inference Platform
- **Focus**: Swedish GPU infrastructure and LLM hosting with EU data residency

---

## 🇨🇳 Chinese Providers

### 21. SiliconFlow 🇨🇳
- **Type**: Chinese First-Party Inference Provider
- **HQ**: Beijing, China
- **Hardware**: H100, H200, AMD MI300
- **Speed Advantage**: 2.3x faster vs avg cloud
- **Models**: 100+
- **Free Models**: ✅ Several free
- **Fine-tuning**: ✅ Yes
- **China Access**: ✅ Direct
- **Int'l Access**: ✅ Available

| Model | Input /1M | Output /1M | Free? |
|-------|-----------|------------|-------|
| DeepSeek V3 | $0.27 | $1.10 | ❌ |
| DeepSeek R1 | $0.55 | $2.19 | ❌ |
| Qwen 3.5 72B | $0.40 | $1.60 | ❌ |
| Qwen 2.5 7B | **FREE** | **FREE** | 🆓 |
| GLM-4-Flash | **FREE** | **FREE** | 🆓 |
| Llama 3.3 70B | $0.40 | $0.40 | ❌ |
| MiniMax M2.5 | $0.20 | $0.80 | ❌ |
| Kimi K2.6 | $0.60 | $2.50 | ❌ |
| FLUX.1-dev (image) | $0.025/img | — | ❌ |

### 22. ModelScope (Alibaba) 🇨🇳
- **Type**: Chinese Open-Source Model Hub (China's HuggingFace)
- **HQ**: Hangzhou, China
- **Models**: 10,000+
- **OpenAI Compatible**: ✅ Yes
- **Enterprise**: ✅ Via Alibaba Cloud
- **China Access**: ✅ Direct (fast)
- **Int'l Access**: ✅ Available
- **Free Tier**: ✅ Yes

**Key Models**: All Qwen family (7B-235B), DeepSeek V3/R1/V4, InternLM series, ChatGLM series, Llama 3/4 family, Mistral family, MiniCPM family

### 23. Baidu Qianfan Platform 🇨🇳
- **Type**: Chinese Enterprise AI Model Platform
- **HQ**: Beijing, China
- **Models**: 50+
- **OpenAI Compatible**: ✅ Yes
- **Free Models**: ✅ ERNIE Speed/Lite free
- **Compliance**: Chinese data regulation compliant

| Model | Input /1M | Output /1M |
|-------|-----------|------------|
| Llama 3.3 70B | $0.28 | $0.56 |
| Mistral 7B | $0.14 | $0.28 |
| Qwen 2.5 72B | $0.20 | $0.60 |
| DeepSeek V3 | $0.27 | $1.10 |
| ChatGLM 4 | $0.10 | $0.10 |
| BLOOMZ 7B | $0.07 | $0.14 |

### 24. Tencent Cloud (HAI / Hunyuan API) 🇨🇳
- **Type**: Chinese Enterprise AI Platform
- **HQ**: Shenzhen, China
- **Models**: 40+
- **OpenAI Compatible**: ✅ Yes
- **WeChat Integration**: ✅ Native

| Model | Input /1M | Output /1M |
|-------|-----------|------------|
| Llama 3.3 70B | $0.28 | $0.56 |
| DeepSeek V3 | $0.27 | $1.10 |
| Qwen 2.5 72B | $0.20 | $0.60 |
| GLM-4 9B | $0.07 | $0.07 |

### 25. VolcEngine (ByteDance) 🇨🇳
- **Type**: Chinese Enterprise Cloud + Model Inference
- **HQ**: Beijing, China
- **Models**: 30+
- **OpenAI Compatible**: ✅ Yes (Ark API)
- **Registration**: ⚠️ CN phone + ID required for direct

| Model | Input /1M | Output /1M |
|-------|-----------|------------|
| Llama 3.3 70B | $0.30 | $0.60 |
| Qwen 2.5 72B | $0.20 | $0.60 |
| DeepSeek R1 | $0.55 | $2.19 |
| Mistral 7B | $0.14 | $0.28 |

### 26. TokenMix (Aggregator for Chinese Models)
- **Type**: OpenAI-Compatible Aggregator for Chinese Models
- **HQ**: China / International
- **Models**: 27+ routes
- **OpenAI Compatible**: ✅ Yes
- **CN Registration Required**: ❌ No
- **Pricing**: No markup

**Models Available**: Qwen 3.6 Plus, Qwen 3.5 Flash, DeepSeek V4 Pro, R1, GLM-5.2, GLM-4.7, Kimi K2.6, K2.7, MiniMax M3, M2.7, MiMo V2 Pro, Doubao Seed 2.0

---

## 🛠️ Gateway / Proxy Tools (Self-Hosted, BYOK)

### 27. LiteLLM
- **Type**: Open-Source Self-Hosted Proxy
- **License**: MIT
- **Cost**: **Free** (self-hosted)
- **Server Cost**: ~$20-50/mo (cheap VPS)
- **Models**: 100+ providers
- **OpenAI Compatible**: ✅ Yes
- **HIPAA/SOC2**: ✅ Self-managed
- **Enterprise**: ✅ LiteLLM Enterprise paid tier

### 28. Portkey
- **Type**: AI Gateway + Observability
- **Platform Fee**: $49/month
- **Models**: All major providers
- **OpenAI Compatible**: ✅ Yes
- **Observability**: ✅ Built-in
- **Enterprise**: ✅ Yes

**Cost at $1,000 API spend**: $1,049 ($49 platform fee + $1,000 API)

### 29. Ofox AI
- **Type**: Zero-Markup API Gateway
- **Markup**: 0%
- **Monthly Fee**: $0
- **OpenAI Compatible**: ✅ OpenAI + Anthropic + Gemini
- **Enterprise**: ✅ Yes

**Example**: DeepSeek V4 Flash at $0.14 in / $0.28 out per 1M tokens — billed at DeepSeek's official rates with **zero markup**

---

## 🤖 Major Model Families & Pricing (Detailed)

### DeepSeek
| # | Model | Release | Input /1M | Output /1M | Cached /1M | Params | API |
|---|-------|---------|-----------|------------|------------|--------|-----|
| 1 | DeepSeek LLM 7B/67B | Nov 2023 | Free OSS | Free | N/A | 7B/67B Dense | ✅ OSS |
| 2 | DeepSeek Coder | Nov 2023 | $0.14 | $0.28 | N/A | 1B-33B | ✅ |
| 3 | DeepSeek V2 | May 2024 | $0.14 | $0.28 | N/A | 236B MoE (21B active) | ✅ |
| 4 | DeepSeek V2-Lite | May 2024 | $0.07 | $0.14 | N/A | 16B MoE (2.4B active) | ✅ |
| 5 | DeepSeek V2.5 | Sep 2024 | $0.14 | $0.28 | N/A | 236B MoE | ✅ |
| 6 | DeepSeek Coder V2 | 2024 | $0.14 | $0.28 | N/A | 236B MoE | ✅ |
| 7 | DeepSeek V3 | Dec 26, 2024 | $0.27 | $1.10 | $0.07 | 671B MoE (37B active) | ✅ |
| 8 | DeepSeek R1-Zero | Jan 2025 | $0.55 | $2.19 | N/A | 671B MoE | ✅ |
| 9 | DeepSeek R1 | Jan 20, 2025 | $0.55 | $2.19 | $0.14 | 671B MoE | ✅ |
| 10-15 | DeepSeek R1 Distill (various) | Jan 2025 | Free OSS | Free | N/A | 1.5B-70B | ✅ OSS |
| 16 | DeepSeek V3-0324 | Mar 2025 | $0.27 | $1.10 | $0.07 | 671B MoE | ✅ |
| 17 | DeepSeek Prover V1.5 | 2025 | $0.55 | $2.19 | N/A | Research | ✅ |
| 18 | Janus Pro 7B | 2025 | $0.27 | $1.10 | N/A | Multimodal | ✅ |
| 19 | DeepSeek V4 Flash | Apr 2026 | $0.07 | $0.14 | $0.02 | 284B total, 13B active | ✅ |
| 20 | DeepSeek V4 Pro | Apr 2026 | $1.30 | $2.60 | $0.10 | 1.6T total, 49B active | ✅ |
| 21 | DeepSeek-Chat (V2/V3) | — | **$0.014** | **$0.028** | N/A | — | ✅ |

**Key Fact**: DeepSeek V4 Pro 75% price discount made permanent May 31, 2026 — output tokens ~34x below GPT-5.5 and ~29x below Claude Opus 4.8.

**Note**: "DeepSeek-Chat" at $0.014/$0.028 per 1M is the cheapest option from a frontier-capable provider (per G2/pricing aggregators), likely referring to V2/V3 tier models on budget providers like DeepInfra.

### MiniMax
| # | Model | Release | Input /1M | Output /1M | Cached /1M | Context | API |
|---|-------|---------|-----------|------------|------------|---------|-----|
| 1-4 | abab1/2/3/5 | 2022-2023 | Legacy | Legacy | N/A | N/A | ❌ Legacy |
| 5 | ABAB 6.5 (MoE) | Apr 17, 2024 | $0.20 | $1.10 | N/A | 256K | ✅ |
| 6 | MiniMax-Text-01 | 2024 | $0.20 | $1.10 | N/A | 1M | ✅ |
| 7 | Hailuo AI Video | Sep 2024 | Per-second | — | N/A | — | ✅ |
| 8 | MiniMax-VL-01 | Jan 2025 | $0.20 | $1.10 | N/A | 1M | ✅ |
| 9 | MiniMax-01 | Jan 2025 | $0.20 | $1.10 | N/A | 1M | ✅ |
| 10 | Speech-02 (TTS) | Apr 2025 | Per-char | — | N/A | — | ✅ |
| 11 | MiniMax-M1 (reasoning) | Jun 2025 | $0.30 | $1.20 | N/A | 1M | ✅ |
| 12 | MiniMax-M1-80k | Jun 2025 | $0.30 | $1.20 | N/A | 80K | ✅ |
| 13 | MiniMax-M2 | Oct 2025 | $0.39 | $1.56 | N/A | 205K | ✅ OSS |
| 14 | MiniMax-M2.1 | Oct 23, 2025 | $0.255 | $1.02 | N/A | 205K | ✅ OSS |
| 15 | MiniMax-M2-her (roleplay) | Jan 23, 2026 | $0.30 | $1.20 | N/A | 66K | ✅ |
| 16 | MiniMax-M2.5 | Feb 12, 2026 | $0.20 | $0.80 | N/A | 205K | ✅ OSS |
| 17 | MiniMax-M2.5-Lightning | Feb 12, 2026 | $0.30 | $2.40 | N/A | 205K | ✅ |
| 18 | MiniMax-M2.7 | Mar 18, 2026 | $0.24 | $0.96 | N/A | 205K | ✅ |
| 19 | MiniMax-M3 | Jun 2026 | $0.40 | $1.60 | N/A | 1M | ✅ |

**Key Fact**: MiniMax M2.5 is a sparse MoE with 230B total / ~10B active params, scoring 80.2% on SWE-Bench Verified.

### Qwen (Alibaba Cloud)
| # | Model | Release | Input /1M | Output /1M | Cached | Context | API |
|---|-------|---------|-----------|------------|--------|---------|-----|
| 1 | Qwen 1.0 (7B/14B/72B) | Sep 2023 | Free OSS | Free | N/A | 8K | ✅ OSS |
| 2 | Qwen 1.5 (0.5B-110B) | Feb 2024 | Free OSS | Free | N/A | 32K | ✅ OSS |
| 3 | Qwen-VL | 2023 | $0.20 | $0.50 | N/A | 4K | ✅ |
| 4 | Qwen-Audio | 2023 | Per-min | — | N/A | — | ✅ |
| 5 | Qwen 2 (0.5B-72B) | Jun 2024 | $0.04 | $0.13 | N/A | 128K | ✅ OSS |
| 6 | Qwen 2-VL | 2024 | $0.20 | $0.50 | N/A | 128K | ✅ |
| 7 | Qwen 2.5 (0.5B-72B) | Sep 2024 | $0.04-$0.40 | $0.12-$1.20 | N/A | 128K | ✅ OSS |
| 8 | Qwen 2.5-Coder | 2024 | $0.07 | $0.12 | N/A | 128K | ✅ OSS |
| 9 | Qwen 2.5-VL | Jan 2025 | $0.40 | $1.20 | N/A | 128K | ✅ |
| 10 | QwQ-32B (reasoning) | Nov 2024 | $0.40 | $1.60 | N/A | 32K | ✅ |
| 11 | QVQ-72B-Preview | Dec 2024 | $0.40 | $1.60 | N/A | 32K | ✅ |
| 12 | Qwen 2.5-Math | 2024 | $0.07 | $0.12 | N/A | 4K | ✅ |
| 13 | Qwen 2.5-Omni | Mar 2025 | $0.30 | $1.20 | N/A | 128K | ✅ |
| 14-16 | Qwen 3 (0.6B/1.7B/4B) | Apr 2025 | Free/$0.05 | Free/$0.40 | N/A | 128K | ✅ OSS |
| 17 | Qwen 3 (8B) | Apr 2025 | **$0.05** | **$0.40** | N/A | 128K | ✅ OSS |
| 18-19 | Qwen 3 (14B/32B) | Apr 2025 | Free | Free | N/A | 128K | ✅ OSS |
| 20 | Qwen 3.5 Flash | 2026 | $0.30 | $3.00 | N/A | — | ✅ |
| 21 | Qwen 3.6 Plus | 2026 | $0.30 | $3.00 | N/A | — | ✅ |
| 22 | Qwen 3.7 Max | 2026 | $1.25 | $5.00 | N/A | 1M | ✅ |

**Key Facts**: 
- Qwen 3 models run in both thinking and non-thinking modes, Apache 2.0 license, trained on 36T tokens across 119 languages
- Qwen3-Coder 480B: 480B total / 35B active, trained on 7.5T tokens (70% code)
- Qwen3.5-Omni and Qwen3.6-Plus (Apr 2026) are proprietary
- Qwen3.7 is API-only, no open weights yet
- ~1 billion downloads by Apr 2026, >50% of all open-source model downloads
- **Cheapest**: Qwen 3 (8B) at $0.05/$0.40 per 1M (not Qwen 2.5 at $0.07)

### Zhipu AI / Z.ai (GLM Family)
| # | Model | Release | Input /1M | Output /1M | Cached /1M | Params | API |
|---|-------|---------|-----------|------------|------------|--------|-----|
| 1 | GLM-130B | 2022 | N/A | N/A | N/A | 130B Dense | ❌ Research |
| 2 | ChatGLM-6B | Mar 2023 | Free OSS | Free | N/A | 6B | ✅ OSS |
| 3 | ChatGLM2-6B | Jun 2023 | Free OSS | Free | N/A | 6B | ✅ OSS |
| 4 | ChatGLM3-6B | Oct 2023 | Free OSS | Free | N/A | 6B | ✅ OSS |
| 5 | GLM-4 | Jan 2024 | $0.10 | $0.10 | N/A | MoE | ✅ |
| 6 | GLM-4V | 2024 | $0.10 | $0.10 | N/A | — | ✅ |
| 7 | GLM-4-Plus | 2024 | $0.70 | $0.70 | N/A | — | ✅ |
| 8 | GLM-4-Long (1M ctx) | 2024 | $0.07 | $0.07 | N/A | — | ✅ |
| 9 | GLM-4-Flash | 2024 | **FREE** | **FREE** | N/A | — | 🆓 |
| 10 | GLM-4-Air | 2024 | $0.07 | $0.07 | N/A | — | ✅ |
| 11 | CogVideoX | 2024 | Per-video | — | N/A | — | ✅ |
| 12 | CogView-3 | 2024 | Per-image | — | N/A | — | ✅ |
| 13 | CogView-4 | 2025 | Per-image | — | N/A | — | ✅ |
| 14 | Ying (text-to-video) | 2024 | Per-video | — | N/A | — | ✅ |
| 15 | AutoGLM (agent) | 2024 | Credits | — | N/A | — | ✅ |
| 16 | GLM-Z1 (reasoning) | Early 2025 | $0.70 | $0.70 | N/A | — | ✅ |
| 17 | GLM-Z1-Flash | 2025 | **FREE** | **FREE** | N/A | — | 🆓 |
| 18 | GLM-4.5 | Jul 2025 | $0.70 | $0.70 | N/A | 100B+ | ✅ OSS |
| 19 | GLM-5 | Feb 2026 | $1.50 | $5.00 | N/A | 744B MoE (40B active) | ✅ |
| 20 | GLM-5.1 | Jul 2026 | $1.50 | $5.00 | N/A | 200K context | ✅ |
| 21 | GLM-5.2 | Jun 2026 | **$1.40** | **$4.40** | N/A | 744B MoE, 1M ctx | ✅ |

**Key Facts**:
- GLM-5: 744B MoE (40B active), trained on Huawei Ascend chips, 28.5T tokens, 77.8% SWE-bench Verified
- GLM-5.2: 744B total, 40B active, 1M context, Intelligence Index v4.1 score 51 (beats MiniMax-M3, DeepSeek V4 Pro, Kimi K2.6)
- GLM-4.7-Flash free with 203K context — strongest zero-cost model from any Chinese provider
- HK IPO Jan 8, 2026 (2513.HK) — world's first listed LLM company

### Moonshot AI (Kimi Family)
| # | Model | Release | Input /1M | Output /1M | Cached /1M | Context | Params | API |
|---|-------|---------|-----------|------------|------------|---------|--------|-----|
| 1 | Moonshot-v1-8k | Oct 2023 | $0.12 | $0.12 | N/A | 8K | — | ✅ |
| 2 | Moonshot-v1-32k | Oct 2023 | $0.24 | $0.24 | N/A | 32K | — | ✅ |
| 3 | Moonshot-v1-128k | Nov 2023 | $0.60 | $0.60 | N/A | 128K | — | ✅ |
| 4 | Kimi (2M-ctx beta) | Mar 2024 | $0.60 | $0.60 | N/A | 2M chars | — | ⚠️ Beta |
| 5 | Kimi Context Caching | Jul 2024 | $0.60 | $0.60 | $0.015 | 128K | — | ✅ |
| 6 | Kimi K1.5 | Jan 20, 2025 | $0.15 | $2.50 | N/A | 128K | Undisclosed | ✅ |
| 7 | Kimi-VL | Apr 2025 | $0.15 | $0.60 | N/A | 128K | 16B MoE (3B active) | ✅ OSS |
| 8 | Kimi-VL-Thinking | Jun 2025 | $0.15 | $0.60 | N/A | 128K | 16B MoE (3B active) | ✅ OSS |
| 9 | Kimi-Dev (coding) | Jun 2025 | $0.60 | $2.50 | N/A | 128K | 72B | ✅ OSS |
| 10 | Kimi-Researcher | Jun 2025 | Credits | — | N/A | — | — | ✅ |
| 11 | Kimi K2 (base) | Jul 2025 | $0.60 | $2.50 | N/A | 128K | 1T MoE (32B active) | ✅ OSS |
| 12 | Kimi K2-Instruct | Jul 2025 | $0.60 | $2.50 | N/A | 128K | 1T MoE (32B active) | ✅ OSS |
| 13 | Kimi K2-Instruct-0905 | Sep 2025 | $0.60 | $2.50 | N/A | 256K | 1T MoE (32B active) | ✅ OSS |
| 14 | Kimi K2 Thinking | 2025 | $0.60 | $2.50 | N/A | 256K | 1T MoE | ✅ |
| 15 | Kimi Linear (edge) | Oct 2025 | $0.20 | $0.80 | N/A | 128K | 48B MoE (3B active) | ✅ |
| 16 | Kimi K2.5 | Jan 2026 | $0.60 | $2.50 | N/A | 256K | 1T MoE (32B active) | ✅ |
| 17 | Kimi K2.6 | 2026 | $0.60 | $2.50 | N/A | 256K | 1T MoE | ✅ |
| 18 | Kimi K2.7 Code | 2026 | $0.15 | $0.60 | N/A | 128K | — | ✅ OSS |

**Key Facts**:
- Kimi K2.5: 1T MoE, 32B active, multimodal, Agent Swarm (100 specialized agents), 50.2% on Humanity's Last Exam
- Kimi K2 series discontinued May 25, 2026 — use Kimi K2.6
- Auto context caching reduces input costs by up to 75%
- Kimi K2.7 Code: best coding performance in Kimi series, low token consumption

---

## 🏢 Other Major Providers (from Complete Master List)

### Anthropic (Claude Family)
| Model | Release | Input /1M | Output /1M | Cached /1M |
|-------|---------|-----------|------------|------------|
| Claude 3 Haiku | Mar 2024 | $0.25 | $1.25 | $0.03 |
| Claude 3 Sonnet | Mar 2024 | $3.00 | $15.00 | $0.30 |
| Claude 3 Opus | Mar 2024 | $15.00 | $75.00 | $1.50 |
| Claude 3.5 Sonnet | Jun 2024 | $3.00 | $15.00 | $0.30 |
| Claude 3.5 Haiku | Nov 2024 | $0.80 | $4.00 | $0.08 |
| Claude 3.7 Sonnet | Feb 2025 | $3.00 | $15.00 | $0.30 |
| Claude Haiku 4 | May 2025 | $0.80 | $4.00 | $0.08 |
| Claude Sonnet 4 | May 2025 | $3.00 | $15.00 | $0.30 |
| Claude Opus 4 | May 2025 | $15.00 | $75.00 | $1.50 |
| Claude Opus 4.5 | Nov 2025 | $5.00 | $25.00 | $0.50 |
| Claude Opus 4.8 | May 2026 | $5.00 | $25.00 | $0.50 |
| **Claude Fable 5** | Jun 2026 | **$10.00** | **$50.00** | $1.00 |
| Claude Sonnet 5 | Jun 2026 | $3.00 | $15.00 | $0.30 |

**Note**: Anthropic leads in caching savings (90% cached-read discount). Most expensive tracked model: **Claude Fable 5** at $10/$50 per 1M.

### xAI (Grok Family)
| Model | Release | Input /1M | Output /1M |
|-------|---------|-----------|------------|
| Grok 1 | Nov 2023 | Open-source | Open-source |
| Grok 1.5 | Early 2024 | $5.00 | $15.00 |
| Grok 2 | Aug 2024 | $2.00 | $10.00 |
| Grok 2 Mini | Aug 2024 | $0.20 | $0.40 |
| Grok 3 | Feb 2025 | $3.00 | $15.00 |
| Grok 4 | Jul 2025 | $3.00 | $15.00 |
| Grok 4 Fast | 2025 | $0.80 | $4.00 |
| Grok 4 Heavy | 2025 | $5.00 | $25.00 |
| Grok 4.1 | 2026 | $2.00 | $10.00 |
| Grok 4.5 | Jul 2026 | $3.00 | $15.00 |

### Google / DeepMind (Gemini)
| Model | Release | Input /1M | Output /1M | Cached /1M |
|-------|---------|-----------|------------|------------|
| Gemini 1.0 Ultra | Dec 2023 | $18.00 | $54.00 | N/A |
| Gemini 1.0 Pro | Dec 2023 | $0.50 | $1.50 | N/A |
| Gemini 1.5 Pro | Feb 2024 | $1.25 | $5.00 | $0.31 |
| Gemini 1.5 Flash | May 2024 | $0.075 | $0.30 | $0.01875 |
| Gemini 2.0 Flash | Dec 2024 | $0.10 | $0.40 | $0.025 |
| Gemini 2.5 Flash | Apr 2025 | $0.15 | $0.60 | $0.0375 |
| Gemini 2.5 Pro | 2025 | $1.25 | $10.00 | $0.31 |
| Gemini 3 Flash | Nov 2025 | $0.10 | $0.40 | $0.025 |
| Gemini 3 Pro | Nov 2025 | $1.25 | $5.00 | $0.31 |
| Gemini 3 Ultra | Nov 2025 | $3.00 | $15.00 | N/A |
| **Gemini 1.5 Flash** | — | **$0.075** | **$0.30** | **$0.01875** |

**Cheapest**: Gemini 1.5 Flash at $0.075/$0.30 per 1M

### Meta (Llama)
| Model | Release | Input /1M | Output /1M |
|-------|---------|-----------|------------|
| Llama 1/2/Code Llama | 2023 | Free (OSS) | Free (OSS) |
| Llama 3 (8B/70B) | Apr 2024 | $0.06 | $0.06 |
| Llama 3.1 (8B/70B/405B) | Jul 2024 | $0.20-$5.00 | $0.20-$15.00 |
| Llama 3.3 70B | Dec 2024 | $0.20 | $0.20 |
| Llama 4 Scout | Apr 2025 | $0.17 | $0.17 |
| Llama 4 Maverick | Apr 2025 | $0.40 | $1.60 |
| Llama 4 Behemoth | Apr 2025 | $2.00 | $8.00 |

### NVIDIA (Nemotron)
| Model | Release | Input /1M | Output /1M |
|-------|---------|-----------|------------|
| Nemotron 2 Nano | 2024 | $0.20 | $0.20 |
| Mistral-NeMo 12B | 2024 | $0.15 | $0.15 |
| Nemotron 3 Nano/Super/Ultra | H1 2026 | $0.42 | $0.42 |
| Nemotron 3 Nano Omni | 2026 | $0.42 | $0.42 |

### OpenAI
| Model | Release | Input /1M | Output /1M | Cached /1M |
|-------|---------|-----------|------------|------------|
| GPT-3.5 | Nov 2022 | $0.50 | $1.50 | N/A |
| GPT-4 | Mar 2023 | $30.00 | $60.00 | N/A |
| GPT-4 Turbo | Nov 2023 | $10.00 | $30.00 | N/A |
| GPT-4o | May 2024 | $2.50 | $10.00 | $1.25 |
| GPT-4o mini | Jul 2024 | $0.15 | $0.60 | $0.075 |
| o1 Preview | Sep 2024 | $15.00 | $60.00 | $7.50 |
| o1 Mini | Sep 2024 | $1.10 | $4.40 | $0.55 |
| o1 (full) | Dec 2024 | $15.00 | $60.00 | $7.50 |
| GPT-4.1 | Apr 2025 | $2.00 | $8.00 | $0.50 |
| GPT-4.1 Mini | Apr 2025 | $0.40 | $1.60 | $0.10 |
| GPT-4.1 Nano | Apr 2025 | $0.10 | $0.40 | $0.025 |
| o3 | Apr 2025 | $10.00 | $40.00 | $2.50 |
| o4-mini | Apr 2025 | $1.10 | $4.40 | $0.275 |
| **GPT-5** | Aug 2025 | **$1.25** | **$5.00** | **$0.31** |
| GPT-5.2 | 2026 | $1.75 | $14.00 | $0.44 |
| GPT-5.3-Codex | 2026 | $2.00 | $10.00 | $0.50 |
| GPT-5.4-Pro | 2026 | $2.50 | $15.00 | $0.63 |
| GPT-5.6 Luna/Terra/Sol | Jul 2026 | Contact Sales | — | N/A |
| gpt-oss-120b/20b | 2025 | Free (OSS) | Free | N/A |

**Note**: GPT-5 is notably cheaper than GPT-4.1 at input tier ($1.25 vs $2.00) while more capable. Regional processing (data residency) endpoints charged 10% uplift for models released on/after March 5, 2026.

### Mistral AI
| Model | Release | Input /1M | Output /1M |
|-------|---------|-----------|------------|
| Mistral 7B | Sep 2023 | Free (OSS) | Free (OSS) |
| Mixtral 8x7B | Dec 2023 | $0.24 | $0.24 |
| Mistral Small | Mar 2024 | $0.10 | $0.30 |
| Mistral Large | Nov 2024 | $2.00 | $6.00 |
| Mistral Nemo 12B | Jul 2024 | **$0.02** | **$0.05** |
| Codestral | May 2024 | $0.30 | $0.90 |
| Pixtral Large | Nov 2024 | $2.00 | $6.00 |
| Ministral 3B | Nov 2024 | $0.04 | $0.04 |
| Ministral 8B | Nov 2024 | $0.10 | $0.10 |
| Mistral Small 3 | Jan 2025 | $0.10 | $0.30 |
| Mistral Medium 3 | May 2025 | $0.40 | $2.00 |
| Devstral Small 1.1 | Jul 2025 | $0.07 | $0.28 |
| Devstral Medium | Jul 2025 | $0.40 | $2.00 |
| Codestral 2508 | Aug 2025 | $0.30 | $0.90 |
| Mistral Medium 3.1 | Aug 2025 | $0.40 | $2.00 |
| Voxtral Small 24B | Oct 2025 | $0.10 | $0.30 |
| **Mistral Large 3 2512** | Dec 2025 | **$0.50** | **$1.50** |
| Ministral 3 3B 2512 | Dec 2025 | $0.10 | $0.10 |
| Ministral 3 8B 2512 | Dec 2025 | $0.15 | $0.15 |
| Mistral Small Creative | Dec 2025 | $0.10 | $0.30 |
| Magistral Small 1.2 | 2026 | $0.50 | $1.50 |
| Magistral Medium | 2026 | $2.00 | $5.00 |
| Mistral Small 2603 | Mar 2026 | $0.15 | $0.60 |
| Mistral Medium 3.5 | Apr 2026 | $1.50 | $7.50 |

**Notes**: Batch processing = 50% discount. No prompt-caching discount (unlike Anthropic's 90%). OpenAI-compatible API.
**Cheapest**: Mistral Nemo 12B at $0.02/$0.05 per 1M

### Microsoft (Phi / Azure AI)
| Model | Release | Input /1M | Output /1M |
|-------|---------|-----------|------------|
| Phi-1/2 | 2023 | Free (OSS) | Free (OSS) |
| Phi-3 Mini/Small/Medium | Apr 2024 | $0.07/$0.07/$0.17 | $0.14/$0.14/$0.17 |
| Phi-3.5 Mini/MoE | 2024 | $0.07/$0.17 | $0.14/$0.17 |
| **Phi-4** | Jan 2025 | **$0.07** | **$0.14** |
| Phi-4-Mini | Mar 2025 | $0.07 | $0.23 |
| Phi-4-Mini Reasoning | Mar 2025 | $0.07 | $0.23 |
| Phi-4 Multimodal | 2025 | $0.05 | $0.10 |
| MAI-1 | 2024 | 🔒 Enterprise | — |
| WizardLM-2 8x22B | Apr 2024 | $0.62 | $0.62 |

**Note**: Phi-4-mini at ~$0.07/$0.23 per 1M = 35x-40x reduction vs GPT-4o.

### Cohere
| Model | Release | Input /1M | Output /1M |
|-------|---------|-----------|------------|
| Command R | Mar 2024 | $0.15 | $0.60 |
| Command R+ | Apr 2024 | $2.50 | $10.00 |
| Command R7B | Dec 2024 | $0.04 | $0.15 |
| Command A | Mar 2025 | $2.50 | $10.00 |
| Aya Expanse 8B/32B | 2024 | $0.50 | $1.50 |
| Embed v3 English/Multilingual | Ongoing | $0.10 | N/A |
| Embed v4 | 2025 | $0.12 | N/A |
| Rerank v3.5/3 Fast/3 Pro | 2024 | $0.001-$0.0025/search | N/A |

**Enterprise**: Model Vault dedicated tier = $4-10/hr/instance ($2,500-6,500/month)

### ByteDance (Doubao / Seed Family)
| Model | Release | Input /1M | Output /1M |
|-------|---------|-----------|------------|
| Doubao 1.5 Lite/Pro | Jan 2025 | $0.044 | $0.088 |
| Doubao 1.6 | Jun 2025 | $0.030 | $0.30 |
| Seed 1.6 Flash | Oct 2025 | $0.022 | $0.219 |
| Seed 1.6 Pro | Oct 2025 | $0.30 | $1.50 |
| Seed 1.8 | Dec 2025 | $0.30 | $1.50 |
| Doubao Seed 2.0 Mini | Feb 2026 | $0.06 | $0.56 |
| Doubao Seed 2.0 Lite | Feb 2026 | $0.13 | $0.76 |
| Doubao Seed 2.0 Pro/Code | Feb 2026 | $0.47 | $2.37 |
| Seedream 3.0 (image) | 2025 | Per-image | — |
| Seedance 1.5 Fast/Pro (video) | 2025 | $0.022/$0.247/sec | — |

**Notes**: Direct API (Volcano Engine Ark) requires CN phone + real-name verification. TokenMix aggregator skips this gate. 19 active Doubao SKUs on TokenMix. Seedance 2.0 "Coming Soon" - not open to third-party developers.

### 01.AI (Yi Family)
| Model | Release | Input /1M | Output /1M |
|-------|---------|-----------|------------|
| Yi-6B/34B | 2023 | Free (OSS) | Free (OSS) |
| Yi-VL | Jan 2024 | $0.40 | $0.40 |
| Yi-1.5 (6B/9B/34B) | May 2024 | $0.14 | $0.14 |
| Yi-Coder 9B | Sep 2024 | $0.38 | $0.38 |
| **Yi-Lightning** | Oct 2024 | **$0.14** | **$0.14** |
| Yi Large/Medium | Nov 2024 | $0.38 | $0.38 |

**Key Fact**: Yi-Lightning at ¥0.99/M (~$0.14) in Oct 2024 — undercutting GPT-4o-mini ($0.26) and ~1/30th of GPT-4 ($4.40).

### Amazon (AWS Bedrock - Titan/Nova)
| Model | Release | Input /1M | Output /1M |
|-------|---------|-----------|------------|
| Titan Text Express/Lite | 2023 | $0.20/$0.15 | $0.60/$0.20 |
| Nova Micro | Nov 2024 | **$0.035** | **$0.14** |
| Nova Lite | Nov 2024 | $0.06 | $0.24 |
| Nova Pro | Nov 2024 | $0.80 | $3.20 |
| Nova Premier | 2025 | $2.50 | $12.50 |
| Nova Canvas/Reel/Act | 2024-2025 | Per-image/Per-second | — |

### Stability AI
| Model | Release | Pricing | Type |
|-------|---------|---------|------|
| Stable Diffusion 2.1/XL 1.0 | 2022-2023 | Free (OSS) | Per-image |
| Stable Diffusion 3/3.5 | 2024 | $0.065/img | Per-image |
| Stable Diffusion 3.5 Turbo | 2024 | $0.04/img | Per-image |
| Stable Fast 3D | 2024 | Per-generation | N/A |

### StepFun AI
| Model | Release | Input /1M | Output /1M |
|-------|---------|-----------|------------|
| Step-1 (300B) | 2023 | $0.70 | $2.10 |
| Step-1V | 2024 | $0.70 | $2.10 |
| Step-1.5V | 2024 | $1.00 | $4.00 |
| Step-2 | 2025 | $1.00 | $4.00 |
| Step-2 Mini | 2025 | $0.20 | $0.80 |
| Step-Audio | 2025 | Per-minute | — |

---

## 📊 Grand Comparison Summary

| # | Company | Total Models | Cheapest Input (1M) | Most Expensive Input (1M) | Commercial API | Enterprise |
|---|---------|--------------|---------------------|---------------------------|----------------|------------|
| 1 | Anthropic | 23 | $0.25 (Haiku) | $10.00 (Fable 5) | ✅ | ✅ |
| 2 | xAI | 14+ | $0.20 (Grok 2 Mini) | $5.00 (Grok Heavy) | ✅ | ✅ |
| 3 | Google | 35+ | $0.075 (Flash) | $18.00 (Gemini Ultra) | ✅ | ✅ Vertex |
| 4 | Meta | 15 | Free/OSS Llama | $2.00 (Behemoth) | ✅ | ✅ |
| 5 | NVIDIA | 15+ | $0.05 (Phi4-Multi) | 🔒 Enterprise | ✅ NIM | ✅ |
| 6 | OpenAI | 27+ | $0.05 (GPT-5-Nano) | $30.00 (GPT-5.5 Pro) | ✅ | ✅ |
| 7 | **DeepSeek** | 11 | **$0.014 (DS-Chat)** | $0.55 (R1) | ✅ | ✅ |
| 8 | MiniMax | 6 | $0.20 (MiniMax-01) | $0.30 (M1) | ✅ | ✅ |
| 9 | Qwen | 10+ | $0.04 (Qwen 2 0.5B) | $0.40 (Qwen 1.x) | ✅ Alibaba | ✅ |
| 10 | Zhipu/Z AI | 8 | $0.10 (GLM-4) | $1.50 (GLM-5.1) | ✅ | ✅ |
| 11 | Moonshot AI | 6 | $0.12 (Kimi) | $0.60 (K2.5) | ✅ | ✅ |
| 12 | Mistral AI | 27+ | **$0.02 (Nemo)** | $2.00 (Large 2) | ✅ | ✅ |
| 13 | Microsoft | 14+ | $0.05 (Phi4-Multi) | $0.62 (WizardLM) | ✅ Azure | ✅ |
| 14 | Cohere | 21 | $0.04 (R7B) | $2.50 (R+/A) | ✅ | ✅ AWS/Azure |
| 15 | ByteDance | 15 | $0.022 (Seed 1.6 Flash) | $0.47 (Seed 2.0 Pro) | ✅ Volcano | ✅ |
| 16 | 01.AI | 8 | $0.14 (Yi-Lightning) | $0.40 (Yi-VL) | ✅ | ✅ |
| 17 | Amazon | 11 | $0.035 (Nova Micro) | $2.50 (Nova Premier) | ✅ Bedrock | ✅ AWS |
| 18 | Stability AI | 9 | $0.04/img (SD Turbo) | $0.065/img | ✅ | ✅ |
| 19 | StepFun | 6 | $0.20 (Step-2 Mini) | $1.00 (Step-2) | ✅ | ✅ |

---

## 🏆 Best Provider by Use Case

| Use Case | Best Provider |
|----------|--------------|
| Highest sustained throughput | Cerebras (~3,000 tok/s) and Groq |
| Lowest first-token latency (chat, agents) | Groq (LPU stack, <1s TTFT) |
| Lowest cost per token | DeepInfra, Novita, and DeepSeek (via DeepInfra) |
| Fine-tuning + inference same platform | Together AI or Fireworks |
| Single API across multiple providers | OpenRouter |
| Image/Video models | Replicate |
| EU Data Sovereignty | Aleph Alpha / Nebius |
| China-Direct Access | SiliconFlow / ModelScope |
| HIPAA Compliant | AWS Bedrock / Baseten |
| Free Self-Hosted | LiteLLM |
| One Key for Everything | OpenRouter |
| Chinese Models, US Data | Featherless / OpenRouter |
| Agentic/Structured Output | Fireworks AI (FireAttention) |
| Enterprise with SLA | AWS Bedrock / Azure Foundry |

---

## ⚠️ Important Disclaimers

1. **Pricing verified** from official pricing pages and independent aggregators as of **July 2026**
2. **Prices change frequently** — SemiAnalysis documented ~40% price increase on H100 GPUs (Oct 2025 - Mar 2026)
3. **LLM API prices dropped ~80%** between early 2025 and early 2026
4. **Chinese provider pricing is especially volatile** — verify directly on each provider's platform
5. **Always verify current rates** before making budgeting, contract, or vendor-selection decisions
6. **OpenAI-compatible API standard** makes it easy to test multiple providers without significant code changes
7. Many teams run **different providers for different use cases**: fast for chat, cheap for batch, GPU cloud for custom models

---

## 🔗 Verification Sources

- **DeepSeek**: platform.deepseek.com/pricing
- **MiniMax**: platform.minimax.io
- **Qwen**: dashscope.aliyuncs.com
- **Zhipu/Z.ai**: open.bigmodel.cn or z.ai
- **Moonshot/Kimi**: platform.moonshot.ai
- **Fireworks AI**: fireworks.ai/pricing
- **Together AI**: together.ai/pricing
- **Groq**: groq.com/pricing
- **DeepInfra**: deepinfra.com/pricing
- **Cerebras**: cerebras.ai/pricing
- **OpenRouter**: openrouter.ai/pricing
- **AWS Bedrock**: aws.amazon.com/bedrock/pricing
- **Azure AI Foundry**: azure.microsoft.com/pricing/details/ai-foundry
- **Google Vertex AI**: cloud.google.com/vertex-ai/pricing
- **Mistral AI**: mistral.ai/pricing
- **Anthropic**: anthropic.com/pricing
- **OpenAI**: platform.openai.com/docs/pricing
- **xAI**: x.ai/api
- **ByteDance/Volcano**: volcanoengine.com
- **SiliconFlow**: siliconflow.com
- **ModelScope**: modelscope.cn
- **Baidu Qianfan**: cloud.baidu.com/product/qianfan
- **Tencent Cloud**: cloud.tencent.com
- **Cohere**: cohere.com/pricing
- **NVIDIA**: nvidia.com/en-us/pricing
- **Amazon Nova**: aws.amazon.com/bedrock/nova
- **Stability AI**: stability.ai/pricing
- **StepFun**: stepfun.ai
- **LiteLLM**: github.com/BerriAI/litellm
- **Portkey**: portkey.ai/pricing
- **Ofox AI**: ofox.ai/pricing

---

*Document generated from "Directly Chat with Frontier AI Search Models" saved July 16, 2026. All prices in USD per 1M tokens unless otherwise noted.*