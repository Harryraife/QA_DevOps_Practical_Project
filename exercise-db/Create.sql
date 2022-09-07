CREATE TABLE IF NOT EXISTS exercisedb.exercises (
    id INT PRIMARY KEY AUTO_INCREMENT,
    exercise_name VARCHAR(50) NOT NULL,
    exercise_sets VARCHAR(10) NOT NULL,
    exercise_reps VARCHAR(10) NOT NULL,
    exercise_accessories VARCHAR(1000) NOT NULL,
    date_generated DATE NOT NULL
);