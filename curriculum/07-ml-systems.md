# Phase 7 - ML Systems

## Required concepts

- CPU, GPU, memory hierarchy, compute, bandwidth, kernels, utilization, and profiling.
- Model parameters, optimizer states, activations, gradients, and memory accounting.
- Data parallelism, DDP, sharding/FSDP, tensor parallelism, pipeline parallelism, and tradeoffs.
- Distributed launch, rendezvous, collective communication, checkpointing, recovery, and stragglers.
- Offline inference, online serving, continuous batching, KV caches, quantization, and autoscaling.
- p50/p95/p99 latency, throughput, goodput, saturation, cost per token, and tail failures.
- Dataset/model/config lineage, experiment tracking, reproducibility, and monitoring.

## Reliability questions

- What happens if one worker fails after other workers advance?
- How is a provider outage distinguished from a model-quality regression?
- Which metrics reveal a queueing bottleneck?
- When does batching improve throughput but harm user experience?

## Exit questions

- When should DDP, FSDP, or tensor parallelism be chosen?
- Why is GPU utilization alone an incomplete performance metric?
- What determines KV-cache memory usage?
- How would you make a distributed eval pipeline idempotent?
