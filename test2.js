import { requestI2CAccess } from "./node_modules/node-web-i2c/index.js";
import NPIX from "@chirimen/neopixel-i2c";
import process from 'process';  // Required to handle signals in Node.js
import http from 'http';         // Import http module

const sleep = msec => new Promise(resolve => setTimeout(resolve, msec));

// LED個数
const neoPixels = 68;
const brightnessFactor = 0.1; // Brightness scale (0.0 to 1.0)

let npix; // グローバル変数としてnpixを定義

main();

async function main() {
    const i2cAccess = await requestI2CAccess();
    const port = i2cAccess.ports.get(1);
    npix = new NPIX(port, 0x41);
    await npix.init(neoPixels);

    // Setup signal handler for Ctrl+C
    process.on('SIGINT', async () => {
        await turnOffLights(npix);
        process.exit();
    });

    // HTTPサーバーの設定
    const server = http.createServer((req, res) => {
        if (req.method === 'GET' && req.url === '/lightup') {
            // ライトアップ処理を非同期で実行
            diagonalRainbowCycle(npix, 20).then(() => {
                turnOffLights(npix);
            }).catch(error => {
                console.error(error);
            });

            res.writeHead(200, { 'Content-Type': 'text/plain' });
            res.end('LEDs are lighting up!\n');
        } else {
            res.writeHead(404, { 'Content-Type': 'text/plain' });
            res.end('Not Found\n');
        }
    });

    // サーバーをポート3000でリッスン
    server.listen(3000, () => {
        console.log('Server is listening on port 3000');
    });
}

// Diagonal rainbow cycle across the LEDs with reduced brightness
async function diagonalRainbowCycle(npix, wait) {
    let grbArray = new Array(neoPixels * 3).fill(0); // Initialize all pixels to off

    for (let j = 0; j < 256 * 5; j++) { // 5 cycles of all colors on wheel
        for (let i = 0; i < neoPixels; i++) {
            // Calculate the diagonal position for the rainbow effect
            let diagonalPos = (i + j) % 256;
            let color = wheel(diagonalPos);
            let r = Math.floor((color >> 16 & 0xff) * brightnessFactor);
            let g = Math.floor((color >> 8 & 0xff) * brightnessFactor);
            let b = Math.floor((color & 0xff) * brightnessFactor);
            grbArray[i * 3] = g;
            grbArray[i * 3 + 1] = r;
            grbArray[i * 3 + 2] = b;
        }
        await npix.setPixels(grbArray);
        await sleep(wait);
    }
}

// Generate rainbow colors across 0-255 positions.
function wheel(WheelPos) {
    WheelPos = 255 - WheelPos;
    if (WheelPos < 85) {
        return (255 - WheelPos * 3) << 16 | (WheelPos * 3) << 8;
    }
    if (WheelPos < 170) {
        WheelPos -= 85;
        return (WheelPos * 3) << 16 | (255 - WheelPos * 3);
    }
    WheelPos -= 170;
    return (WheelPos * 3) << 8 | (255 - WheelPos * 3) << 16;
}

// Function to turn off all the lights
async function turnOffLights(npix) {
    let grbArray = new Array(neoPixels * 3).fill(0); // Set all pixels to off (black)
    await npix.setPixels(grbArray);
}
