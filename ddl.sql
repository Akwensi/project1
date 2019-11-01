CREATE SCHEMA stackoverflow_filtered;

CREATE TABLE stackoverflow_filtered."results" ( 
    "users_id" text NOT NULL,
    "display_name" text null,
    "views" text null,
    "reputation" text null,
    "updated_at" text null,
    "location" text null,
    "city" text null,
    "country" text null,
    "questions_id" text null,
    "questions_user_id" text null,
    "title" text null,
    "body" text null,
    "accepted_answer_id" text null,
    "score" text null,
    "view_count" text null,
    "comment_count" text null,
    "created_at" text null,
    "answers_id" text null,
    "answers_user_id" text null,
    "question_id" text null,
    "answers_body" text null,
    "answers_score" text null,
    "answers_comment_count" text null,
    "answers_created_at" text null 
);
