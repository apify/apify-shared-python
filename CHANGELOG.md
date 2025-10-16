# Changelog

All notable changes to this project will be documented in this file.

<!-- git-cliff-unreleased-start -->
## 2.1.1 - **not yet released**

### 🚀 Features

- **consts:** Add actor permission level env var ([#52](https://github.com/apify/apify-shared-python/pull/52)) ([43b9e81](https://github.com/apify/apify-shared-python/commit/43b9e819fae71ac73afa40d406be4d1871dc9960)) by [@stepskop](https://github.com/stepskop)


<!-- git-cliff-unreleased-end -->
## [2.1.0](https://github.com/apify/apify-shared-python/releases/tag/v2.1.0) (2025-09-05)

### 🚀 Features

- Add ActorPermissionLevel enum ([#51](https://github.com/apify/apify-shared-python/pull/51)) ([52a1f73](https://github.com/apify/apify-shared-python/commit/52a1f73e2d2b2f988820562aa03785f255aa0cc7)) by [@tobice](https://github.com/tobice)


## [2.0.0](https://github.com/apify/apify-shared-python/releases/tag/v2.0.0) (2025-08-13)

### Chore

- [**breaking**] Drop support for Python 3.8 ([#45](https://github.com/apify/apify-shared-python/pull/45)) ([bb0a9fa](https://github.com/apify/apify-shared-python/commit/bb0a9faabf30e5259066a8e35b93941b2ebfbfea)) by [@vdusek](https://github.com/vdusek)
- [**breaking**] Drop support for Python 3.9 ([#46](https://github.com/apify/apify-shared-python/pull/46)) ([7372fd6](https://github.com/apify/apify-shared-python/commit/7372fd640fe64831f24e254c7c84592d43922c48)) by [@vdusek](https://github.com/vdusek)

### Refactor

- [**breaking**] Remove unused code from models, types, and utils ([#43](https://github.com/apify/apify-shared-python/pull/43)) ([ea02f2c](https://github.com/apify/apify-shared-python/commit/ea02f2c818bb7c365c56529146bf021b5b2575f5)) by [@vdusek](https://github.com/vdusek)
- [**breaking**] Remove deprecated enum values ([#48](https://github.com/apify/apify-shared-python/pull/48)) ([1d24989](https://github.com/apify/apify-shared-python/commit/1d249897fa9a5a4c608f797925e82a9c679a430b)) by [@vdusek](https://github.com/vdusek)


## [1.5.0](https://github.com/apify/apify-shared-python/releases/tag/v1.5.0) (2025-08-05)

### 🚀 Features

- Add create_hmac_signature and create_storage_content_signature ([#44](https://github.com/apify/apify-shared-python/pull/44)) ([70d146f](https://github.com/apify/apify-shared-python/commit/70d146f933adcf2cbe2f224c07efa603fb7ae77a)) by [@danpoletaev](https://github.com/danpoletaev)


## [1.4.1](https://github.com/apify/apify-shared-python/releases/tag/v1.4.1) (2025-04-28)

### 🚀 Features

- Add FOLLOW_USER_SETTING to generalAccess enum ([#38](https://github.com/apify/apify-shared-python/pull/38)) ([15eb5e8](https://github.com/apify/apify-shared-python/commit/15eb5e8d3aae7c906282137e31c9aedcf279ddf3)) by [@tobice](https://github.com/tobice)

### 🐛 Bug Fixes

- Remove check-changelog pre-commit hook ([#39](https://github.com/apify/apify-shared-python/pull/39)) ([306c42c](https://github.com/apify/apify-shared-python/commit/306c42ca23553391ed148acc32df75f71de15b21)) by [@tobice](https://github.com/tobice)


## [1.4.0](https://github.com/apify/apify-shared-python/releases/tag/v1.4.0) (2025-04-11)

### 🚀 Features

- Add general access enum to consts ([#34](https://github.com/apify/apify-shared-python/pull/34)) ([6de5a2f](https://github.com/apify/apify-shared-python/commit/6de5a2f901625def4b45a2af1d24f8d4ab33664c)) by [@tobice](https://github.com/tobice)


## [1.3.2](https://github.com/apify/apify-shared-python/releases/tag/v1.3.2) (2025-03-20)

### 🐛 Bug Fixes

- Add CLI origin ([#32](https://github.com/apify/apify-shared-python/pull/32)) ([1e3360c](https://github.com/apify/apify-shared-python/commit/1e3360c20636c0d8c9d01dcb4d9e196647e9afb0)) by [@janbuchar](https://github.com/janbuchar)


## [1.3.1](https://github.com/apify/apify-shared-python/releases/tag/v1.3.1) (2025-03-07)

### 🐛 Bug Fixes

- Add STANDBY option to MetaOrigin enum ([#30](https://github.com/apify/apify-shared-python/pull/30)) ([0da682f](https://github.com/apify/apify-shared-python/commit/0da682f128bab62bf47264eb42e88b34245b41c8)) by [@janbuchar](https://github.com/janbuchar)


## [1.3.0](https://github.com/apify/apify-shared-python/releases/tag/v1.3.0) (2025-03-04)

### Chore

- [**breaking**] Remove unused consts ([#28](https://github.com/apify/apify-shared-python/pull/28)) ([b56da6e](https://github.com/apify/apify-shared-python/commit/b56da6e3652c157d087513727e5496530381d0d1)) by [@vdusek](https://github.com/vdusek)


## [1.2.1](https://github.com/apify/apify-shared-python/releases/tag/v1.2.1) (2024-12-06)

### 🐛 Bug Fixes

- Turn `ACTOR_BUILD_TAGS` into a comma-separated list env var ([#27](https://github.com/apify/apify-shared-python/pull/27)) ([cbe2ddd](https://github.com/apify/apify-shared-python/commit/cbe2ddd5ec4312acdaf8f35308191c26cbc7dfc7)) by [@fnesveda](https://github.com/fnesveda)


## [1.2.0](https://github.com/apify/apify-shared-python/releases/tag/v1.2.0) (2024-12-05)

### 🚀 Features

- Add new environment variables ([#26](https://github.com/apify/apify-shared-python/pull/26)) ([55a8542](https://github.com/apify/apify-shared-python/commit/55a8542639ba9db2e151174412a7cc72883e9679)) by [@fnesveda](https://github.com/fnesveda)


## [1.1.2](https://github.com/apify/apify-shared-python/releases/tag/v1.1.2) (2024-07-04)

### 🚀 Features

- **consts:** Add actor standby consts ([#21](https://github.com/apify/apify-shared-python/pull/21)) ([7871d7b](https://github.com/apify/apify-shared-python/commit/7871d7b1d1ce52e4ce6af587e88b95fa842c6280)) by [@jirimoravcik](https://github.com/jirimoravcik)


## [1.0.2](https://github.com/apify/apify-shared-python/releases/tag/v1.0.2) (2023-08-01)

### 🚀 Features

- Use Actor env vars ([#5](https://github.com/apify/apify-shared-python/pull/5)) ([53d27d9](https://github.com/apify/apify-shared-python/commit/53d27d9551ddb143ae26e33b2bb7f7e9a06871d0)) by [@jirimoravcik](https://github.com/jirimoravcik)


## [1.0.0](https://github.com/apify/apify-shared-python/releases/tag/v1.0.0) (2023-07-25)


<!-- generated by git-cliff -->