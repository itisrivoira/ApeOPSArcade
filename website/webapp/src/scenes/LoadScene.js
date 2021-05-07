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
        //General Texts
        this.load.image("youWon", "src/assets/youWon.png");

        //MenuScene buttons
        this.load.image("title", "src/assets/title.png");
        this.load.image("play_button", "src/assets/play_button.png");
        this.load.image("options_button", "src/assets/options_button.png");
        this.load.image("background", "src/assets/bg.png");

        //OptionsScene buttons
        this.load.image("OptionsScene-toggleOn", "src/assets/buttons/toggle_on.png");
        this.load.image("OptionsScene-toggleOff", "src/assets/buttons/toggle_off.png");

        this.load.image("OptionsScene-commands", "src/assets/buttons/button_commands_black.png");
        this.load.image("OptionsScene-back", "src/assets/buttons/button_back_black.png");

        //OptionsScene Labels
        this.load.image("OptionsScene-musicLabel", "src/assets/option_music_toggle.png");
        this.load.image("OptionsScene-effectsLabel", "src/assets/option_effects_toggle.png");

        //CommandsScene Labels
        this.load.image("CommandsScene-leftLabel", "src/assets/commands_sub/left.png");
        this.load.image("CommandsScene-rightLabel", "src/assets/commands_sub/right.png");
        this.load.image("CommandsScene-upLabel", "src/assets/commands_sub/up.png");
        this.load.image("CommandsScene-downLabel", "src/assets/commands_sub/down.png");
        this.load.image("CommandsScene-returnLabel", "src/assets/commands_sub/return.png");
        this.load.image("CommandsScene-closeLabel", "src/assets/commands_sub/close.png");

        //CommandsScene keys
        this.load.image("CommandsScene-leftarrowkey", "src/assets/commands_sub/cmds/leftarrowkey.png");
        this.load.image("CommandsScene-rightarrowkey", "src/assets/commands_sub/cmds/rightarrowkey.png");
        this.load.image("CommandsScene-uparrowkey", "src/assets/commands_sub/cmds/uparrowkey.png");
        this.load.image("CommandsScene-downarrowkey", "src/assets/commands_sub/cmds/downarrowkey.png");
        this.load.image("CommandsScene-esc_key", "src/assets/commands_sub/cmds/esckey.png");
        this.load.image("CommandsScene-alt_f4_key", "src/assets/commands_sub/cmds/alt_f4key.png");

        //LVLScene assets
        this.load.image("LVLScene-menuFight", "src/assets/lvlAssets/menu_ingame_fight.png");
        this.load.image("LVLScene-menuItems", "src/assets/lvlAssets/menu_ingame_items.png");

        this.load.image("LVLScene-menuHiddenButton", "src/assets/lvlAssets/blank_menu_hiddenButton.png");
        this.load.image("LVLScene-menuHiddenButton2", "src/assets/lvlAssets/blank_menu_hiddenButton2.png");

        this.load.image("LVLScene-hpHeartFull", "src/assets/lvlAssets/hp_heart.png");
        this.load.image("LVLScene-hpHeartEmpty", "src/assets/lvlAssets/hp_heart_gray.png");
        this.load.image("LVLScene-hpHeartHalf", "src/assets/lvlAssets/hp_heart_half.png");
        this.load.image("LVLScene-hpHeartHalfEnemy", "src/assets/lvlAssets/hp_heart_half_enemy.png");

        //LVLScene protagonist
        this.load.image("LVLScene-protag", "src/assets/lvlAssets/protag.png");
        this.load.image("LVLScene-protagIcon", "src/assets/lvlAssets/protag_Icon.png");
        this.load.image("LVLScene-protagActionKick", "src/assets/lvlAssets/protagKick.png");
        this.load.image("LVLScene-protagActionPunch", "src/assets/lvlAssets/protagPunch.png");
        this.load.image("LVLScene-protagActionShoot", "src/assets/lvlAssets/protagShoot.png");
        this.load.image("LVLScene-protagActionWin", "src/assets/lvlAssets/protagWin.png");

        //LVLScene first enemy
        this.load.image("LVLScene-brigadiereRuspa", "src/assets/lvlAssets/brigadiereRuspa.png");
        this.load.image("LVLScene-brigadiereRuspaIcon", "src/assets/lvlAssets/brigadiereRuspa_Icon.png");
        this.load.image("LVLScene-brigadiereRuspaHit", "src/assets/lvlAssets/brigadiereRuspa_hit.png");

        //LVL2Scene Assets
        this.load.image("LVL2Scene-menu", "src/assets/lvl2Assets/menu_ingame_fight2.png");
        this.load.image("LVL2Scene-protagActionFire", "src/assets/lvl2Assets/protagFire.png");
        this.load.image("LVL2Scene-brigadiereMattarella", "src/assets/lvl2Assets/chefNibba.png");
        this.load.image("LVL2Scene-brigadiereMattarellaFire", "src/assets/lvl2Assets/chefNibba_Fire.png");
        this.load.image("LVL2Scene-brigadiereMattarellaHit", "src/assets/lvl2Assets/chefNibba_hit.png");
        this.load.image("LVL2Scene-brigadiereMattarellaIcon", "src/assets/lvl2Assets/chefNibba_icon.png");

        //background music
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
        this.scene.start(CST.SCENES.MENU, { HELLO: "LoadScene HELLO", flagSound: 1 });
    }
}