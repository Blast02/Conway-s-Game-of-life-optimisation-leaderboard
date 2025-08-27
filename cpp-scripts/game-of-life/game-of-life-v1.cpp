// Version 1 of conway's game of life in c++ no optimisation done, just my first c++ project
// SDL3.dll required

#define SDL_MAIN_USE_CALLBACKS 1 
#include <SDL3/SDL.h>
#include <SDL3/SDL_main.h>
#include <iostream>
#include <vector>
#include <random>
#include <chrono>


const int width = 1280;
const int height = 720;
const int cell = 10;
const int tickrate = 60; // tick per second
const int tickdelay = 1000 / tickrate;


static SDL_Window* window = NULL;
static SDL_Renderer* renderer = NULL;

int step_counter = 0; // benchmark variable
const int max_steps = 5000; // number of steps
bool benchmark_done = false;
std::chrono::high_resolution_clock::time_point start_time;

const int white = (255, 255, 255);
const int black = (0, 0, 0);
const int green = (0, 255, 0);

const int rows = height / cell;
const int cols = width / cell;


std::vector<std::vector<int>> current_grid(rows, std::vector<int>(cols));
std::vector<std::vector<int>> next_grid(rows, std::vector<int>(cols));


void init_grid(std::vector<std::vector<int>>& grid, unsigned int seed = 49) { // Seed
    std::mt19937 rng(seed);
    std::uniform_int_distribution<int> dist(0, 1);

    for (int y = 0; y < rows; y++) {
        for (int x = 0; x < cols; x++) {
            grid[y][x] = dist(rng);
        }
    }
}


void draw_grid() // Draw white grid
{
    SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);

    for (int x = 0; x <= width; x += cell)
    {
        SDL_RenderLine(renderer, x, 0, x, height);
    }
    for (int y = 0; y <= height; y += cell)
    {
        SDL_RenderLine(renderer, 0, y, width, y);
    }
}


void draw_alive(const std::vector<std::vector<int>>& current_grid) // Draw green cells
{
    SDL_SetRenderDrawColor(renderer, 0, 255, 0, 255);
    for (int y = 0; y < rows; y++)
    {
        for (int x = 0; x < cols; x++)
        {
            if (current_grid[y][x] == 1)
            {
                SDL_FRect rect = { (float)x * cell, (float)y * cell, (float)cell, (float)cell };
                SDL_RenderFillRect(renderer, &rect);
            }
        }
    }
}


int counts_neighbors(const std::vector<std::vector<int>>& grid, int y, int x) // Count the number of neighbors
{
    int count = 0;
    for (int dy = -1; dy <= 1; dy++) {
        for (int dx = -1; dx <= 1; dx++) {
            if (dy == 0 && dx == 0) continue;

            int ny = (y + dy + rows) % rows;
            int nx = (x + dx + cols) % cols;

            count += grid[ny][nx];
        }
    }
    return count;
}


std::vector<std::vector<int>> alive(const std::vector<std::vector<int>>& grid) // Calculate the next state of the grid
{
    std::vector<std::vector<int>> next(rows, std::vector<int>(cols, 0));

    for (int y = 0; y < rows; y++) {
        for (int x = 0; x < cols; x++) {
            int neighbors = counts_neighbors(grid, y, x);

            if (grid[y][x] == 0 && neighbors == 3) {
                next[y][x] = 1;
            }
            else if (grid[y][x] == 1 && (neighbors == 2 || neighbors == 3)) {
                next[y][x] = 1;
            }
        }
    }
    return next;
}


SDL_AppResult SDL_AppInit(void** appstate, int argc, char* argv[]) // Init SDL window
{
    SDL_SetAppMetadata("Game of life", "1.0", "base-cpp");

    if (!SDL_Init(SDL_INIT_VIDEO)) {
        SDL_Log("Couldn't initialize SDL: %s", SDL_GetError());
        return SDL_APP_FAILURE;
    }

    if (!SDL_CreateWindowAndRenderer("Game of life", width, height, 0, &window, &renderer)) {
        SDL_Log("Couldn't create window/renderer: %s", SDL_GetError());
        return SDL_APP_FAILURE;
    }

    init_grid(current_grid); // Generate 0's and 1's of the grid
    SDL_Delay(1000); // leave time for SDL to generate the window
    start_time = std::chrono::high_resolution_clock::now();

    return SDL_APP_CONTINUE;
}


SDL_AppResult SDL_AppEvent(void* appstate, SDL_Event* event) // handle input
{
    if (event->type == SDL_EVENT_QUIT) {
        return SDL_APP_SUCCESS;
    }
    return SDL_APP_CONTINUE;
}


SDL_AppResult SDL_AppIterate(void* appstate) // While true loop
{
    Uint32 tickstart = SDL_GetTicks();

    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
    SDL_RenderClear(renderer); // Clear window for next frame

    draw_alive(current_grid); // Draw green cells
    draw_grid(); // Draw white grid
    next_grid = alive(current_grid); // Calculate the next state of the grid
    current_grid = next_grid; 

    step_counter++;
    if (step_counter >= max_steps) { // benchark
        auto end_time = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> elapsed = end_time - start_time;

        double total_seconds = elapsed.count();
        double steps_per_sec = step_counter / total_seconds;

        std::cout << "Benchmark terminé !" << std::endl;
        std::cout << "Nombre de steps : " << step_counter << std::endl;
        std::cout << "Temps total : " << total_seconds << " secondes" << std::endl;
        std::cout << "Performance : " << steps_per_sec << " steps/s" << std::endl;
        return SDL_APP_SUCCESS;
    }

    /*    Uint32 ticktime = SDL_GetTicks() - tickstart; // Limite speed
        if (tickdelay > ticktime)
            SDL_Delay(tickdelay - ticktime); */

    SDL_RenderPresent(renderer);

    return SDL_APP_CONTINUE;
}

/* This function runs once at shutdown. */
void SDL_AppQuit(void* appstate, SDL_AppResult result)
{

}

