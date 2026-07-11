# Project 7 - Distributed Eval and Serving Platform

## Question

Can hundreds of model/task combinations run reliably while preserving lineage and separating quality failures from system failures?

## Build

- Open-model server using vLLM or an equivalent runtime.
- Queue and distributed workers.
- Idempotent task IDs, retries, timeouts, cancellation, and checkpointing.
- Versioned model, prompt, dataset, scaffold, and judge metadata.
- Structured traces and Prometheus-style metrics.
- Dashboard for quality, error rate, latency, throughput, tokens, and cost.

## Experiments

- Concurrency sweep and saturation point.
- Batch-size latency/throughput tradeoff.
- Failure injection and recovery.
- Quantization quality/performance comparison.

## Acceptance criteria

- Duplicate execution cannot double-count a result.
- p50/p95/p99 and throughput are reported under a declared load.
- Quality comparisons use identical evaluation conditions.
- Runbook distinguishes model, data, harness, provider, and infrastructure failures.
