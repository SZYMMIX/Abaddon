# Pygame Doom Engine (Raycasting 3D)

A custom-built pseudo-3D game engine written from scratch in **Python** using **Pygame**. 
This project is an educational deep dive into the classic rendering techniques used in early 90s first-person shooters like *Wolfenstein 3D* and *Doom*.

![Gameplay Screenshot](assets\docs\gameplay_screenshot.png)

## 🚀 Current Features

### 1. 3D World Rendering (Raycasting)
*   **DDA Algorithm:** Fast and precise grid-collision detection for rays, ensuring stable framerates and pixel-perfect wall edges.
*   **Fisheye Correction:** Mathematical correction (`math.cos`) to prevent spherical distortion at the edges of the screen.
*   **Texture Mapping:** Dynamic vertical slicing and scaling of 2D images (`subsurface`) to create textured 3D walls.
*   **Depth Shading:** Walls get progressively darker the further away they are from the player, creating a sense of depth.

### 2. Player Mechanics
*   **Vector Movement:** Normalized diagonal movement.
*   **Mouse Look:** First-person camera rotation with relative mouse movement (`pygame.mouse.get_rel()`) and hidden cursor.
*   **Hitbox Collision:** An Axis-Aligned Bounding Box collision system that allows sliding along walls without getting stuck or clipping the camera through textures.

### 3. Entities & Interaction
*   **3D Sprites:** Rendering 2D enemy images in 3D space, ensuring they always face the camera while scaling correctly with distance.
*   **Z-Buffer:** Sprites are correctly occluded by walls using a custom depth buffer generated during the raycasting phase.
*   **Painter's Algorithm:** Sprites are sorted back-to-front before rendering to handle overlapping objects correctly.
*   **Hitscan Shooting:** Instant-hit weapon mechanics with a central crosshair check against the Z-Buffer and enemy bounding boxes.
*   **Animated Weapons:** State-machine based weapon animations synced to the game's framerate.

## 🛠️ Technologies
*   **Python 3.x**
*   **Pygame**

## 📦 Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/SZYMMIX/Abaddon.git
    cd Abaddon
    ```

2.  **Install requirements:**
    ```bash
    pip install pygame
    ```

3.  **Run the game:**
    ```bash
    python main.py
    ```

## 🎮 Controls

| Key / Mouse | Action |
| :--- | :--- |
| **W, A, S, D** | Move (Forward, Back, Strafe Left/Right) |
| **Mouse** | Look around (Camera rotation) |
| **LMB / Space** | Shoot |
| **ESC** | Exit Game |

## 🚧 Roadmap (Next Steps)
The engine is currently a functional prototype. Planned features include:
- [ ] **Enemy Animations:** Idle, Walk, Pain, and Death states for sprites.
- [ ] **Enemy AI:** A* Pathfinding to allow enemies to navigate the maze and chase the player.
- [ ] **Map Loader:** Parsing text files to generate levels dynamically instead of hardcoding arrays.
- [ ] **Sound Effects:** Adding spatial audio and weapon sounds.

## 📄 License
This project is open-source and created for educational purposes to understand retro 3D graphics programming.