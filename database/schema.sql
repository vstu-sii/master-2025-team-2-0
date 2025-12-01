-- database/schema.sql (серверная часть)
CREATE TABLE recipes (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    ingredients JSONB,  -- JSON
    steps TEXT,        -- JSON
    cooking_time INTEGER,
    calories INTEGER,
    difficulty TEXT,
    source TEXT CHECK(source IN ('ai', 'official')) DEFAULT 'ai',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_ingredients_gin ON recipes 
USING GIN (ingredients);