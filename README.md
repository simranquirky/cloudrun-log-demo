# Cloud Run to OpenObserve Demo (Python)

This is a simple Flask app that logs messages directly to OpenObserve using its HTTP API. Designed to run on Google Cloud Run.

## Setup

### 1. Get OpenObserve Info

Get the following from your OpenObserve dashboard:

- `OPENOBSERVE_URL`
- `OPENOBSERVE_ORG` 
- `OPENOBSERVE_STREAM` - a name of your choice
- `OPENOBSERVE_API_KEY`

### 2. Deploy to Cloud Run

```bash
gcloud run deploy cloudrun-log-demo \
  --source . \
  --region us-central1 \
  --platform managed \
  --allow-unauthenticated \
  --set-env-vars OPENOBSERVE_URL=https://api.openobserve.ai,\
OPENOBSERVE_ORG=your-org,\
OPENOBSERVE_STREAM=cloudrun-logs,\
OPENOBSERVE_API_KEY=your-api-key
