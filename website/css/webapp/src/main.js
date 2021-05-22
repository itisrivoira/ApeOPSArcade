import { LoadScene } from "./scenes/LoadScene.js";
import { MenuScene } from "./scenes/MenuScene.js";
import { OptionsScene } from "./scenes/OptionsScene.js";
import { CommandsScene } from "./scenes/CommandsScene.js";
import { LVL1Scene } from "./scenes/LVL1Scene.js";
import { LVL2Scene } from "./scenes/LVL2Scene.js";
import { LVL3Scene } from "./scenes/LVL3Scene.js";
let game = new Phaser.Game({
    width: 800,
    height: 440,
    parent: 'gameDiv',
    physics: {
        default: 'arcade',
        arcade: {
            //gravity: { y: 400 },
            debug: false
        }
    },
    scene: [
        LoadScene, MenuScene, LVL1Scene, LVL2Scene, LVL3Scene, OptionsScene, CommandsScene
    ]
});