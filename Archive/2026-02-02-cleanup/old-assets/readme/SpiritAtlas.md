# SpiritAtlas

Privacy-first Android app that delivers spiritual and relationship insights using modern mobile architecture and consent-gated AI assistance.

## Funder Snapshot
- Product: Mobile experience combining multiple spiritual systems with a premium visual identity.
- Differentiation: Privacy-first design, multi-provider AI routing, and modular Clean Architecture.
- Execution: Extensive documentation, security hardening, and verified test suites.

## What Is Built
- Multi-module Android app with clean boundaries (app, feature, domain, data, core).
- Core calculation engines for numerology, astrology, ayurveda, and human design.
- Consent gates for any cloud AI calls with local-first behavior.
- Encrypted storage and SSL pinning.
- 100+ custom visual assets optimized across Android densities.

## Architecture (Module Flow)
```
app -> feature -> domain
core -> domain
data -> domain
```

## Engineering Depth
- Jetpack Compose UI with Material 3 design system.
- Hilt dependency injection and WorkManager background tasks.
- Dedicated test suites for core calculation modules.
- Security and compliance documentation.

## Documented Results
- 119 custom images across 5 Android densities.
- Core calculation test suites with full passing runs (see test logs in repo).

## Tech Stack
- Kotlin, Android SDK 34, Gradle 8.x
- Jetpack Compose, Hilt, WorkManager
- EncryptedSharedPreferences, network security config

## Repository Structure
```
app/            Android app host and navigation
core/           Reusable calculation and UI modules
domain/         Business rules and models
data/           Repositories, storage, network
feature/        Feature modules (home, profile, consent, compatibility, settings)
```

## Build and Test (Quick)
```
./gradlew :app:assembleDebug
./gradlew test
```

## Documentation
- SECURITY.md and DISCLAIMER.md define safety and usage boundaries.
- CHANGELOG.md, docs/, and reports in the repo capture implementation history.

## License
See LICENSE in the repo.
