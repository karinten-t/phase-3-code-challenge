# phase-3-code-challenge
articles-system/
├── lib/                      # Core application code
│   ├── models/               # Domain models
│   │   ├── author.py         # Author model and operations
│   │   ├── article.py        # Article model and operations
│   │   └── magazine.py       # Magazine model and operations
│   ├── db/                   # Database components
│   │   ├── connection.py     # Database connection handling
│   │   ├── schema.sql        # Database schema definition
│   │   └── seed.py           # Test data generation
│   └── debug.py              # Interactive debugging console
├── tests/                    # Comprehensive test suite
├── scripts/                  # Utility scripts
│   ├── setup_db.py           # Database initialization
│   └── run_queries.py        # Example query runner(not required)
└── README.md                 # Project documentation