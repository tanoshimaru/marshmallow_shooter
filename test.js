import { requestI2CAccess } from "./node_modules/node-web-i2c/index.js";
import NPIX from "@chirimen/neopixel-i2c";
const sleep = msec => new Promise(resolve => setTimeout(resolve, msec));

// LED個数
const neoPixels = 68;

main();

async function main() {
    const i2cAccess = await requestI2CAccess();
    const port = i2cAccess.ports.get(1);
    const npix = new NPIX(port, 0x41);
    await npix.init(neoPixels);

    await nPixTest(npix);
}

async function setPattern(npix, pattern) {
    // パターン設定
    const grbArray = [];
    for (const color of pattern) {
        const r = color >> 16 & 0xff;
        const g = color >> 8 & 0xff;
        const b = color & 0xff;
        grbArray.push(g);
        grbArray.push(r);
        grbArray.push(b);
    }
    await npix.setPixels(grbArray);
}

async function moji_pattern(moji){
    var pattern  = Array(neoPixels);
    pattern.fill(0);
    for(const num of moji){
        pattern[num] = 0x001100;
    }
    return pattern;
}

async function moji_nagasu_pattern(pattern){
    var pattern_next = Array(neoPixels);
    pattern_next.fill(0);
    for(let i=0; i<7; i++){
        for(let j=0; j<8; j++){
            let index = (8*j)+i;
            pattern_next[index] = pattern[index+1];
        }
    }
    return pattern_next;
}

async function moji_nagasu_pattern_2(moji_pattern, num){
    var pattern_next = Array(neoPixels);
    pattern_next.fill(0);
    for(let i=0; i<=num; i++){
        for(let j=0; j<8; j++){
            let index = (8*j)+i;
            pattern_next[index+7-num] = moji_pattern[index];
        }
    }

    return pattern_next;
}

async function moji_nagasu(npix, moji_pattern){
    var pattern = Array(neoPixels);
    pattern.fill(0);
    for(let i=0; i<7; i++){
        pattern = await moji_nagasu_pattern_2(moji_pattern, i);
        await setPattern(npix, pattern);
        await sleep(100);
    }

    var pattern = moji_pattern;
    for(let i=0; i<8; i++){
        pattern = await moji_nagasu_pattern(pattern)
        await setPattern(npix, pattern);
        await sleep(100);
    }
}


async function nPixTest(npix) {
    await npix.setGlobal(0, 0, 0);

    var ta = [9,10,11,15,20,22,27,30,38,41,42,43,45,52,53,54,55,61]
    var no = [11,12,18,22,25,29,31,33,36,39,42,44,46,51,52,53]
    var ma = [10,12,13,14,15,19,20,21,22,23,28,34,35,36,37,38,39,44,50,51,52,53,54,55,60]
    var ru = [11,12,13,14,18,21,22,26,31,35,36,37,38,45,52,59,60,61,62]


    // // たのまる を永遠に流す
    // var pattern = Array(neoPixels)
    // while(true){
    //     pattern = await moji_pattern(ta)
    //     setPattern(npix, pattern);
    //     await sleep(1000);

    //     pattern = await moji_pattern(no)
    //     setPattern(npix, pattern);
    //     await sleep(1000);

    //     pattern = await moji_pattern(ma)
    //     setPattern(npix, pattern);
    //     await sleep(1000);

    //     pattern = await moji_pattern(ru)
    //     setPattern(npix, pattern);
    //     await sleep(1000);
    // }


    // 最初に中央にたのまる　をだして永遠に流す
    var pattern_ta = Array(neoPixels);
    pattern_ta = await moji_pattern(ta);

    var pattern_no = Array(neoPixels);
    pattern_no = await moji_pattern(no);

    var pattern_ma = Array(neoPixels);
    pattern_ma = await moji_pattern(ma);

    var pattern_ru = Array(neoPixels);
    pattern_ru = await moji_pattern(ru);

    while(true){
        moji_nagasu(npix, pattern_ta)
        await sleep(3000);

        moji_nagasu(npix, pattern_no)
        await sleep(3000);

        moji_nagasu(npix, pattern_ma)
        await sleep(3000);

        moji_nagasu(npix, pattern_ru)
        await sleep(3000);
    }

    // await npix.setGlobal(0, 0, 0);
}
