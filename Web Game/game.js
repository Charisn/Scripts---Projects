const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

const car = {
  x: 50,
  y: 50,
  width: 50,
  height: 30,
  speed: 5,
  moveUp: function() { this.y -= this.speed },
  moveDown: function() { this.y += this.speed },
  moveLeft: function() { this.x -= this.speed },
  moveRight: function() { this.x += this.speed },
  draw: function() {
    ctx.fillStyle = '#FF0000';
    ctx.fillRect(this.x, this.y, this.width, this.height);
  }
}

const checkpoints = [
  {
    x: 150,
    y: 150,
    info: 'Checkpoint 1'
  },
  {
    x: 300,
    y: 300,
    info: 'Checkpoint 2'
  },
  {
    x: 450,
    y: 450,
    info: 'Checkpoint 3'
  }
];

function drawCheckpoints() {
  checkpoints.forEach(checkpoint => {
    ctx.fillStyle = '#0000FF';
    ctx.fillRect(checkpoint.x, checkpoint.y, 10, 10);
    ctx.font = 'bold 16px Arial';
    ctx.fillStyle = '#FFF';
    ctx.fillText(checkpoint.info, checkpoint.x + 20, checkpoint.y + 10);
});
}

function clearCanvas() {
ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function updateCanvas() {
clearCanvas();
drawCheckpoints();
car.draw();
}

function checkCollision() {
checkpoints.forEach((checkpoint, index) => {
if (car.x < checkpoint.x + 10 &&
car.x + car.width > checkpoint.x &&
car.y < checkpoint.y + 10 &&
car.y + car.height > checkpoint.y) {
alert(checkpoint.info);
checkpoints.splice(index, 1);
}
});
}

updateCanvas();

document.addEventListener('keydown', e => {
switch (e.key) {
case 'ArrowUp':
car.moveUp();
break;
case 'ArrowDown':
car.moveDown();
break;
case 'ArrowLeft':
car.moveLeft();
break;
case 'ArrowRight':
car.moveRight();
break;
}
checkCollision();
updateCanvas();
});

document.getElementById('up').addEventListener('click', () => {
car.moveUp();
checkCollision();
updateCanvas();
});

document.getElementById('down').addEventListener('click', () => {
car.moveDown();
checkCollision();
updateCanvas();
});

document.getElementById('left').addEventListener('click', () => {
car.moveLeft();
checkCollision();
updateCanvas();
});

document.getElementById('right').addEventListener('click', () => {
car.moveRight();
checkCollision();
updateCanvas();
});
class Car {
    constructor(x, y, speed) {
      this.x = x;
      this.y = y;
      this.speed = speed;
      this.width = 50;
      this.height = 50;
      this.frameIndex = 0;
      this.tickCount = 0;
      this.ticksPerFrame = 4;
      this.numberOfFrames = 4;
      this.image = new Image();
      this.image.src = 'car-spritesheet.png';
    }
  
    draw() {
      ctx.drawImage(
        this.image,
        this.frameIndex * this.width,
        0,
        this.width,
        this.height,
        this.x,
        this.y,
        this.width,
        this.height
      );
    }
  
    update() {
      this.tickCount += 1;
      if (this.tickCount > this.ticksPerFrame) {
        this.tickCount = 0;
        if (this.frameIndex < this.numberOfFrames - 1) {
          this.frameIndex += 1;
        } else {
          this.frameIndex = 0;
        }
      }
    }
  
    moveUp() {
      this.y -= this.speed;
      this.frameIndex = 1;
    }
  
    moveDown() {
      this.y += this.speed;
      this.frameIndex = 0;
    }
  
    moveLeft() {
      this.x -= this.speed;
      this.frameIndex = 2;
    }
  
    moveRight() {
      this.x += this.speed;
      this.frameIndex = 3;
    }
  }
  