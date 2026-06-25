# Credentialed Service Probes

The service probes check whether local `.env` credentials authenticate without printing secrets and
without mutating vendor state.

```bash
python scripts/probe_service_keys.py --env-file .env
python scripts/probe_service_keys.py --env-file .env --no-fail
```

The probes are intentionally read-only:

- Firecrawl: reads recent team activity.
- GitHub: reads the authenticated user.
- Cloudflare: verifies the API token and, when `CLOUDFLARE_ACCOUNT_ID` is set, reads that account.
- ClickHouse Cloud: reads visible organizations through the Cloud API.
- Stripe: reads the account attached to the secret key.

ClickHouse has two credential layers. `CLICKHOUSE_CLOUD_KEY_ID` and
`CLICKHOUSE_CLOUD_KEY_SECRET` prove ClickHouse Cloud control-plane access. The official ClickHouse
MCP server also needs database connection variables such as `CLICKHOUSE_HOST`, `CLICKHOUSE_USER`,
`CLICKHOUSE_PASSWORD`, `CLICKHOUSE_DATABASE`, and `CLICKHOUSE_ALLOW_WRITE_ACCESS=false` for
credentialed end-to-end query traces.

Use test or sandbox credentials for mutation-capable services. A live Stripe key should only be used
for read-only checks unless the task explicitly requires live account changes.
