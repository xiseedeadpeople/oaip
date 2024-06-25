class SnakeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = Snake()
        self.food = Food()
        self.obstacles = []

    def update(self):
        pass
    
    def draw(self):
        pass
    
    def check_collision(self):
        pass


class Snake:
    def __init__(self):
        self.head = (0, 0)
        self.body = [(0, 0)]
        self.direction = "RIGHT"
        self.length = 1

    def move(self):
        pass
    
    def grow(self):
        pass
    
    def change_direction(self, direction):
        pass
    
    def check_collision(self):
        pass


class Food:
    def __init__(self):
        self.position = (5, 5)

    def respawn(self):
        pass
    
    def check_collision(self):
        pass


class Obstacle:
    def __init__(self, position):
        self.position = position

    def check_collision(self):
        pass


# Пример использования
if __name__ == "__main__":
    game = SnakeGame(20, 10)
    game.snake.move()
    game.food.respawn()
