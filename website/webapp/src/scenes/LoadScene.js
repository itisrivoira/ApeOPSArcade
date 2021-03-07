import { CST } from "../CST.js";
export class LoadScene extends Phaser.Scene {
    constructor() {
        super({
            key: CST.SCENES.LOAD
        })
    }
    init() {

    }
    preload() {
        this.load.image("title", "src/assets/title.png");
        this.load.image("play_button", "src/assets/play_button.png");
        this.load.image("options_button", "src/assets/options_button.png");
        this.load.image("background", "src/assets/bg.png");

        //OptionsScene buttons
        this.load.image("OptionsScene-toggleOn", "src/assets/buttons/toggle_on.png");
        this.load.image("OptionsScene-toggleOff", "src/assets/buttons/toggle_off.png");

        //OptionsScene Labels
        this.load.image("OptionsScene-musicLabel", "src/assets/option_music_toggle.png");
        this.load.image("OptionsScene-effectsLabel", "src/assets/option_effects_toggle.png");

        this.load.audio("bgMusic", "src/assets/sounds/bg_music.mp3");

        var progressBar = this.add.graphics();
        var progressBox = this.add.graphics();
        progressBox.fillStyle(0x222222, 0.8);
        progressBox.fillRect(240, 190, 320, 50);

        var width = this.cameras.main.width;
        var height = this.cameras.main.height;
        var loadingText = this.make.text({
            x: width / 2,
            y: height / 2 - 50,
            text: 'Loading...',
            style: {
                font: '20px monospace',
                fill: '#ffffff'
            }
        });
        loadingText.setOrigin(0.5, 0.5);

        var percentText = this.make.text({
            x: width / 2,
            y: height / 2 - 5,
            text: '0%',
            style: {
                font: '18px monospace',
                fill: '#ffffff'
            }
        });
        percentText.setOrigin(0.5, 0.5);

        var assetText = this.make.text({
            x: width / 2,
            y: height / 2 + 50,
            text: '',
            style: {
                font: '18px monospace',
                fill: '#ffffff'
            }
        });
        assetText.setOrigin(0.5, 0.5);

        this.load.on('progress', function(value) {
            console.log(value);
            percentText.setText(parseInt(value * 100) + '%');
            progressBar.clear();
            progressBar.fillStyle(0xffffff, 1);
            progressBar.fillRect(250, 200, 300 * value, 30);
        });

        this.load.on('fileprogress', function(file) {
            console.log(file.src);
            assetText.setText('Loading asset: ' + file.key);
        });

        this.load.on('complete', function() {
            console.log('complete');
            progressBar.destroy();
            progressBox.destroy();

            loadingText.destroy();
            percentText.destroy();
            assetText.destroy();
        });
    }
    create() {
        this.scene.start(CST.SCENES.MENU, "LoadScene HELLO");
    }
}