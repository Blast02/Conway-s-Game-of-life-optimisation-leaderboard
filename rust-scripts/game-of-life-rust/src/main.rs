use macroquad::prelude::*;
use std::{usize, vec};
use ::rand::Rng;
use rand_mt::Mt;
use std::time::Instant;


const WIDTH: u16 = 1280;
const HEIGHT: u16 = 720;
const CELL: u16 = 2;

const MAXSTEPS: u16 = 500;

const ROWS: usize = (HEIGHT / CELL) as usize;
const COLS: usize = (WIDTH / CELL) as usize;

fn init_grid(current_grid: &mut [Vec<u16>]) {
    let seed: u32 = 49;
    let mut rng = Mt::new(seed);

    for y in 0..ROWS {
        for x in 0..COLS {
            current_grid[y][x] = rng.gen_range(0..=1);
        }
    }
}

fn draw_grid() {
    for x in (0..WIDTH).step_by(CELL as usize).map(|x| x as f32) {
        draw_line(x, 0.0, x, HEIGHT as f32, 0.5, WHITE);
    }

    for y in (0..HEIGHT).step_by(CELL as usize).map(|y| y as f32) {
        draw_line(0.0, y, WIDTH as f32, y, 0.5, WHITE);
    }
}

fn draw_alive(current_grid: &[Vec<u16>]){
    let cell = CELL as f32;
    for y in 0..ROWS {
        for x in  0..COLS {
            if current_grid[y][x] == 1 {
                draw_rectangle(x as f32 * cell, y as f32 * cell, cell - 1.0, cell - 1.0, GREEN);
            }
        }
    }
}

fn count_neighbors(current_grid: &[Vec<u16>], y: usize, x: usize, rows: usize, cols: usize) -> u16 {
    let y_up    = if y == 0        { rows - 1 } else { y - 1 };
    let y_down  = if y + 1 == rows { 0 }          else { y + 1 };

    let x_left  = if x == 0        { cols - 1 } else { x - 1 };
    let x_right = if x + 1 == cols { 0 }          else { x + 1 };

    let mut count: u16 = 0;
    count += current_grid[y_up][x_left];
    count += current_grid[y_up][x];
    count += current_grid[y_up][x_right];

    count += current_grid[y][x_left];

    count += current_grid[y][x_right];

    count += current_grid[y_down][x_left];
    count += current_grid[y_down][x];
    count += current_grid[y_down][x_right];

    count
}

fn alive(current_grid: &[Vec<u16>], next_grid: &mut [Vec<u16>]) {
   for y in 0..ROWS {
        for x in 0..COLS {
            let neighbors = count_neighbors(current_grid, y, x, ROWS, COLS);
            let cur = current_grid[y][x];
            next_grid[y][x] = match (cur, neighbors) {
                (0, 3) => 1,
                (1, 2) | (1, 3) => 1,
                _ => 0,
            };
        }
    }
}

fn window_conf() -> Conf {
    Conf {
        window_title: "Game of Life".to_owned(),
        window_width: 1280,
        window_height: 720,
        fullscreen: false,
        ..Default::default()
    }
}
#[macroquad::main(window_conf)]
async fn main() {

    let mut current_grid: Vec<Vec<u16>> = vec![vec![0; COLS]; ROWS];
    let mut next_grid: Vec<Vec<u16>> = vec![vec![0; COLS]; ROWS];
    init_grid(&mut current_grid);

    let start_time = Instant::now();
    let mut step_counter: usize = 0;

    loop {
        clear_background(BLACK);

        draw_alive(&current_grid);
        draw_grid();

        alive(&current_grid, &mut next_grid);
        std::mem::swap(&mut current_grid, &mut next_grid);

        step_counter += 1;

        if step_counter >= (MAXSTEPS as usize) {
            let end_time = Instant::now();
            let elapsed = end_time.duration_since(start_time);
            let total_seconds = elapsed.as_secs_f64();
            let steps_per_sec = (step_counter as f64) / total_seconds;

            println!("Benchmark terminé !");
            println!("Nombre de steps : {}", step_counter);
            println!("Temps total : {:.6} secondes", total_seconds);
            println!("Performance : {:.2} steps/s", steps_per_sec);
            let start_time = get_time();
            while get_time() - start_time < 100.0 {
                next_frame().await;
            }
            std::process::exit(0);

        }
        next_frame().await;
    }
}