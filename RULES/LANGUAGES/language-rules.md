# Language-Specific Rules Collection

---

## TypeScript / JavaScript Rules

### Strict TypeScript Configuration
```json
// tsconfig.json strict settings
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "noPropertyAccessFromIndexSignature": true,
    "exactOptionalPropertyTypes": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "verbatimModuleSyntax": true,
    "isolatedModules": true,
    "moduleDetection": "force",
    "skipLibCheck": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext"
  }
}
```

### Rules

1. **No `any` type** — Use `unknown` + type narrowing instead
2. **No type assertions** — Prefer type guards: `if ('prop' in obj)`
3. **No non-null assertions** — Handle null/undefined explicitly
4. **Prefer `const` over `let`** — Immutability first
5. **No `enum`** — Use `as const` objects: `const Status = { Active: 'active', ... } as const`
6. **Use `satisfies` operator** — Type-safe object literals: `config satisfies Config`
7. **Discriminated unions** — `type Result = { ok: true; data: T } | { ok: false; error: Error }`
8. **Branded types** — `type UserId = string & { readonly __brand: 'UserId' }`
9. **No barrel files in large projects** — Direct imports for tree-shaking
10. **Zod for runtime validation** — Schema-first validation at boundaries

### ESLint Configuration (Flat Config)
```javascript
// eslint.config.js
import eslint from '@eslint/js';
import tseslint from 'typescript-eslint';
import prettier from 'eslint-config-prettier';

export default tseslint.config(
  eslint.configs.recommended,
  ...tseslint.configs.strictTypeChecked,
  ...tseslint.configs.stylisticTypeChecked,
  prettier,
  {
    rules: {
      '@typescript-eslint/no-explicit-any': 'error',
      '@typescript-eslint/no-non-null-assertion': 'error',
      '@typescript-eslint/prefer-nullish-coalescing': 'error',
      '@typescript-eslint/prefer-optional-chain': 'error',
      '@typescript-eslint/strict-boolean-expressions': 'error',
      '@typescript-eslint/switch-exhaustiveness-check': 'error',
      '@typescript-eslint/no-floating-promises': 'error',
      '@typescript-eslint/no-misused-promises': 'error',
      '@typescript-eslint/require-await': 'error',
      'no-console': ['warn', { allow: ['warn', 'error'] }],
      'prefer-const': 'error',
      'no-var': 'error',
      'eqeqeq': ['error', 'always'],
    },
  }
);
```

---

## Python Rules

### Ruff Configuration
```toml
# pyproject.toml
[tool.ruff]
target-version = "py312"
line-length = 99
src = ["src", "tests"]

[tool.ruff.lint]
select = [
  "E",    # pycodestyle errors
  "W",    # pycodestyle warnings
  "F",    # pyflakes
  "I",    # isort
  "N",    # pep8-naming
  "UP",   # pyupgrade
  "B",    # flake8-bugbear
  "S",    # flake8-bandit (security)
  "A",    # flake8-builtins
  "C4",   # flake8-comprehensions
  "DTZ",  # flake8-datetimez
  "ICN",  # flake8-import-conventions
  "PIE",  # flake8-pie
  "PT",   # flake8-pytest-style
  "RET",  # flake8-return
  "SIM",  # flake8-simplify
  "TCH",  # flake8-type-checking
  "ARG",  # flake8-unused-arguments
  "PTH",  # flake8-use-pathlib
  "ERA",  # eradicate (commented code)
  "RUF",  # Ruff-specific rules
  "PERF", # perflint
  "FURB", # refurb
]
ignore = [
  "S101",  # assert used (OK in tests)
  "S104",  # bind to 0.0.0.0 (OK in containerized apps)
]

[tool.ruff.lint.per-file-ignores]
"tests/**/*.py" = ["S101", "ARG"]

[tool.ruff.lint.isort]
known-first-party = ["myapp"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
docstring-code-format = true

[tool.mypy]
python_version = "3.12"
strict = true
warn_return_any = true
disallow_any_explicit = false
disallow_untyped_defs = true
no_implicit_reexport = true
warn_unused_ignores = true
show_error_codes = true
```

### Rules

1. **Type hints everywhere** — All functions, return types, class attributes
2. **Pydantic for data models** — `BaseModel` with field validation
3. **`pathlib.Path`** — Never use `os.path` string manipulation
4. **Structural pattern matching** — `match/case` for complex branching
5. **Context managers** — `with` for all resource management
6. **f-strings only** — No `.format()` or `%` formatting
7. **`dataclasses` for simple data** — `@dataclass(frozen=True, slots=True)`
8. **Async with `asyncio`** — `async/await` for I/O-bound operations
9. **`collections.abc`** — Use abstract types: `Sequence`, `Mapping`, `Iterable`
10. **Never `import *`** — Explicit imports always

---

## Go Rules

### golangci-lint Configuration
```yaml
# .golangci.yml
run:
  timeout: 5m
  tests: true
  go: "1.22"

linters:
  enable:
    - errcheck        # Check error returns
    - govet           # Vet examines Go source code
    - staticcheck     # Staticcheck analysis
    - unused          # Check unused code
    - gosimple        # Simplification suggestions
    - ineffassign     # Detect inefficient assignments
    - typecheck       # Type checking
    - gocritic        # Opinionated linter
    - gocyclo         # Cyclomatic complexity
    - gofmt           # Format check
    - goimports       # Import formatting
    - misspell        # Spelling mistakes
    - unconvert       # Unnecessary conversions
    - unparam         # Unused parameters
    - prealloc        # Slice preallocation
    - nilerr          # nil error returns
    - errorlint       # Error wrapping issues
    - exhaustive      # Exhaustive switch checks
    - sqlclosecheck   # SQL close checking
    - bodyclose       # HTTP body close checking
    - contextcheck    # Context propagation

linters-settings:
  gocritic:
    enabled-checks:
      - appendAssign
      - boolExprSimplify
      - captLocal
      - defaultCaseOrder
      - dupBranchBody
      - elseif
      - ifElseChain
      - nestingReduce
      - rangeValCopy
      - sloppyLen
      - switchTrue
      - typeSwitchVar
      - underef
      - unslice

  gocyclo:
    min-complexity: 15

  errcheck:
    check-type-assertions: true
    check-blank: true

issues:
  max-issues-per-linter: 50
  max-same-issues: 3
  exclude-use-default: false
```

### Rules

1. **Error handling** — Always check errors: `if err != nil { return fmt.Errorf("context: %w", err) }`
2. **Wrap errors** — Use `%w` for error wrapping, not `%v`
3. **Context propagation** — First parameter is `ctx context.Context`
4. **Table-driven tests** — `map[string]struct{ ... }` test cases
5. **No init()** — Avoid init functions; use explicit initialization
6. **Interfaces at consumer** — Define interfaces where they're used, not implemented
7. **Small interfaces** — 1-3 methods maximum
8. **Channel direction** — `chan<-` or `<-chan` in function signatures
9. **`defer` for cleanup** — Always defer resource cleanup
10. **No global state** — Pass dependencies explicitly via structs

---

## Rust Rules

### Clippy Configuration
```toml
# clippy.toml
cognitive-complexity-threshold = 25
too-many-arguments-threshold = 7
type-complexity-threshold = 250

# Cargo.toml
[lints.clippy]
pedantic = "warn"
nursery = "warn"
unwrap_used = "deny"
expect_used = "warn"
panic = "deny"
todo = "warn"
dbg_macro = "deny"
print_stdout = "warn"
print_stderr = "warn"
```

### Rules

1. **No `.unwrap()`** — Use `?` operator or match/if-let
2. **Ownership-first design** — Minimize `Clone`, prefer borrowing
3. **`thiserror` for library errors** — Derive Error implementations
4. **`anyhow` for application errors** — Context-rich error chains
5. **Newtype pattern** — `struct UserId(u64)` for type safety
6. **Builder pattern** — For complex struct construction
7. **`#[must_use]`** — On functions where ignoring result is a bug
8. **Lifetimes only when needed** — Let elision handle simple cases
9. **`Arc<Mutex<T>>`** — For shared mutable state across threads
10. **Prefer iterators** — `.iter().filter().map().collect()` over loops

---

## Java / Kotlin Rules

### Rules (Java)

1. **Records for data** — `record User(String name, String email) {}`
2. **Sealed interfaces** — `sealed interface Shape permits Circle, Square`
3. **Pattern matching** — `if (obj instanceof String s) { use(s); }`
4. **`Optional` for nullable returns** — Never return null from public methods
5. **No checked exceptions** — Wrap in `RuntimeException` subtypes
6. **No mutable collections** — `List.of()`, `Map.of()`, `Set.of()`
7. **`var` for local variables** — When type is obvious from context
8. **Text blocks** — `"""multi-line"""` for SQL, JSON, HTML
9. **Virtual threads** — `Thread.ofVirtual().start()` for I/O-bound tasks
10. **Avoid null** — Use `Optional`, `@Nullable`, or sealed types

### Rules (Kotlin)

1. **Data classes** — `data class User(val name: String, val email: String)`
2. **Null safety** — Use `?.`, `?:`, never `!!`
3. **Extension functions** — Add behavior without inheritance
4. **Coroutines** — `suspend fun` for async, `Flow` for streams
5. **Sealed classes** — Exhaustive when expressions
6. **Value classes** — `@JvmInline value class UserId(val id: String)`
7. **No utility classes** — Use top-level functions
8. **Scope functions** — `let`, `run`, `apply`, `also`, `with` appropriately
9. **Immutable by default** — `val` over `var`, `listOf` over `mutableListOf`
10. **Named arguments** — `createUser(name = "John", email = "j@e.com")`
