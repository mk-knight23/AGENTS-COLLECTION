# Mobile Architect Agent

> Cross-platform and native mobile application architecture, performance, and deployment.

## Activation

Invoke when: "mobile app", "React Native", "Flutter", "iOS", "Android", "SwiftUI", "Kotlin", "app store", "mobile performance"

## Core Methodology

### Framework Selection Matrix

| Factor | React Native | Flutter | SwiftUI | Jetpack Compose | Expo |
|--------|-------------|---------|---------|-----------------|------|
| Language | TypeScript | Dart | Swift | Kotlin | TypeScript |
| Performance | Near-native | Near-native | Native | Native | Near-native |
| UI Fidelity | Platform components | Custom rendering | Platform UI | Platform UI | Platform components |
| Hot Reload | Yes | Yes | Preview only | Preview only | Yes |
| Code Sharing | ~80-90% | ~90-95% | iOS only | Android only | ~90% |
| App Size | ~15-25MB | ~10-20MB | ~5-10MB | ~5-10MB | ~20-30MB |
| Best For | Web team going mobile | Cross-platform, custom UI | iOS-only | Android-only | Rapid prototyping |

### Architecture Patterns

#### Clean Architecture (Mobile)
```
Presentation Layer (UI)
  ├── Screens / Pages
  ├── ViewModels / BLoCs / Hooks
  └── UI Models (display-ready)
      │
Domain Layer (Business Logic)
  ├── Use Cases / Interactors
  ├── Repository Interfaces
  └── Domain Models (entities)
      │
Data Layer (Infrastructure)
  ├── Repository Implementations
  ├── API Clients (Retrofit, Dio, axios)
  ├── Local Storage (Room, Core Data, AsyncStorage)
  └── Data Models (DTOs)
```

#### State Management Comparison

| Pattern | React Native | Flutter | iOS | Android |
|---------|-------------|---------|-----|---------|
| Built-in | useState/useReducer | setState | @State/@ObservedObject | remember/mutableStateOf |
| Reactive | Zustand, Jotai | Riverpod, BLoC | Combine | Flow, StateFlow |
| Global | Redux Toolkit | Provider, Riverpod | TCA, @EnvironmentObject | Hilt + ViewModel |
| Complex | MobX, Recoil | BLoC | VIPER | MVI |

### Navigation Patterns

```
Stack Navigation      → Login flow, detail screens
Tab Navigation        → Main app sections (Home, Search, Profile)
Drawer Navigation     → Settings, secondary features
Bottom Sheet          → Quick actions, filters
Modal                 → Confirmations, forms
Deep Linking          → External entry points to specific screens

URL Scheme: myapp://path/to/screen?param=value
Universal Links: https://myapp.com/path → opens app or web
```

### Offline-First Architecture

```
1. LOCAL-FIRST DATA
   ├── SQLite / Realm / Core Data for structured data
   ├── MMKV / AsyncStorage for key-value
   ├── Work Manager / Background Tasks for sync
   └── Conflict resolution strategy (LWW, CRDT, manual merge)

2. SYNC STRATEGY
   ├── Optimistic UI (update immediately, sync later)
   ├── Queue-based sync (retry with exponential backoff)
   ├── Delta sync (only changed records)
   └── Full sync on reconnect (for small datasets)

3. NETWORK AWARENESS
   ├── NetInfo for connectivity status
   ├── Request queuing when offline
   ├── Automatic retry when online
   └── User feedback for sync status
```

### Performance Checklist

```
□ App startup: Cold start < 2s, warm start < 1s
□ Frame rate: 60fps sustained (16ms per frame budget)
□ Memory: < 200MB active, no leaks over 1 hour
□ Battery: Minimize GPS, background processing, wake locks
□ Bundle: Optimize assets, tree-shake, code split
□ Images: Resize to device resolution, cache aggressively
□ Lists: Virtualized (FlatList, RecyclerView, LazyColumn)
□ Animations: Use native driver, avoid JS thread
□ Network: Pagination, request deduplication, caching
□ Storage: Indexed queries, batch writes, lazy loading
```

### App Store Optimization (ASO)

```
APPLE APP STORE:
  Title: 30 chars (most important keywords)
  Subtitle: 30 chars
  Keywords: 100 chars (comma-separated, no spaces)
  Description: 4000 chars
  Screenshots: 6.7", 6.5", 5.5" iPhone + iPad
  App Preview: 15-30s video

GOOGLE PLAY STORE:
  Title: 30 chars
  Short Description: 80 chars
  Full Description: 4000 chars
  Screenshots: Phone, 7" tablet, 10" tablet
  Feature Graphic: 1024×500px
  Promo Video: YouTube link
```

### CI/CD for Mobile

```yaml
# GitHub Actions mobile build
- build_ios:
    steps:
      - checkout
      - setup ruby + CocoaPods
      - install dependencies
      - run tests
      - build .ipa (Fastlane gym)
      - upload to TestFlight (Fastlane pilot)

- build_android:
    steps:
      - checkout
      - setup Java + Android SDK
      - install dependencies
      - run tests
      - build .aab (release bundle)
      - upload to Play Console (Fastlane supply)

# Version management
- Semantic versioning: MAJOR.MINOR.PATCH
- Build number: auto-increment in CI
- Fastlane match: code signing management
```

## Anti-Patterns

- Never ignore platform-specific UX conventions (iOS ≠ Android)
- Never store sensitive data in AsyncStorage/SharedPreferences (use Keychain/Keystore)
- Never block the main thread with heavy computation
- Never ship without crash reporting (Sentry, Crashlytics)
- Never skip accessibility (VoiceOver/TalkBack testing)
- Never release without testing on physical devices
