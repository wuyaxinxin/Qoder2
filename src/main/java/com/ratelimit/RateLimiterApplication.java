// 模型决策
package com.ratelimit;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.scheduling.annotation.EnableScheduling;

/**
 * Distributed Rate Limiter Application
 * 
 * Enterprise-grade distributed API rate limiting system with:
 * - Token Bucket algorithm (allows burst traffic)
 * - Sliding Window algorithm (smooth rate limiting)
 * - Multi-dimensional limiting (user, IP, endpoint)
 * - User tier-based configuration
 * - Redis-backed distributed state
 * - Graceful degradation with local caching
 */
@SpringBootApplication
@EnableAsync
@EnableScheduling
public class RateLimiterApplication {

    public static void main(String[] args) {
        SpringApplication.run(RateLimiterApplication.class, args);
    }
}
