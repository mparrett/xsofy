# Xs of Y — mobile fork

A personal fork of [nooga/xsofy](https://github.com/nooga/xsofy) with mobile UI: bottom-bar D-pad, info row, hold-to-repeat, char-size toggle.

A roguelike written in [let-go](https://github.com/nooga/let-go), where the magic system is a lisp. 

> Note: This is not finished! It's playable but mild peril and uscheduled explosions are to be expected.

**[Play in your browser](https://mparrett.github.io/xsofy/)**

The live build is auto-deployed from the [`play` branch](https://github.com/mparrett/xsofy/tree/play). This fork also depends on experimental [let-go](https://github.com/mparrett/let-go/tree/play) primitives (the HTML/WASM bridge, an SAB ring buffer for input, a few touch-UI ergonomics) that haven't been upstreamed yet.

![screenshot](xsofy.gif)

Every run generates a new title (_Gazebos of Mounting Dread_), a new quest (_retrieve the Spatula of Futility_), and a new set of rune mappings. The runes are secretly symbols, spells are s-expressions. You have root access to the dungeon's reality engine but the man pages are in a dead language that changes every boot.

The power curve is inverted - early game is desperate survival, late game is applied theology with inadequate safety margins.

Meanwhile the dungeon is trying to kill you through more conventional means. Spiders shoot web cones that trap you while goblins close in. Slimes split when you hit them. Trolls regenerate. Set something on fire and it panics, runs through grass, ignites the grass, ignites more creatures - it's fine, everything is fine. Push an ogre into lava. Push a goblin into another goblin. Push yourself into a chasm by accident. Chasms are educational.

Written in ~6900 lines of [let-go](https://github.com/nooga/let-go) - a Clojure dialect on a Go bytecode VM. Persistent data structures all the way down. No dependencies. 6ms startup. Runs natively or [in the browser](https://mparrett.github.io/xsofy/) via WASM.

If you like how this game looks check out [Brogue](https://sites.google.com/site/broguegame/) - my main inspiration.

## Running

Easiest: the [live build](https://mparrett.github.io/xsofy/).

For native terminal play, this fork needs the matching let-go runtime (the `brew install let-go` stable version doesn't yet have the primitives the mobile bridge depends on):

```bash
git clone https://github.com/mparrett/let-go && cd let-go
git checkout play && go build -o lg .
cd ../xsofy && ../let-go/lg main.lg
```

If you're just playing in the terminal and want stock upstream, the parent project at [nooga/xsofy](https://github.com/nooga/xsofy) installs cleanly with brew's `let-go`.
