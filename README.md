# Player Character Also Party Talks
Fear &amp; Hunger 2: Termina Mod. <br>

<h2> What is it?</h2>
This mod makes it so that your chosen main character (PC) also participates in "Party Talk" (the skill). This includes interjections made by and towards the PC. This also means that you will end up talking to yourself out loud when alone in your party.

<h2>Recommended for a first playthrough?</h2>
I don't necessarily recommend against it, because this will just make it so that your PC's personality is more discernible and you will get extra interactions in the Party Talk because of it. I'd only advise you to not use the Party Talk until you're out of the Prologue (aka when you walk out the train into the forest for the first time). More on that in the Problems / Bugs section below, but you might be mildly spoiled there, but in case you decide to install it then just don’t activate the Party Talk until you’re done with the prologue.

<h2>Problems or Bugs?</h2>
No bugs that I'm aware of so far, but there are odd behaviors that will happen because of how the game structured the Party Talk mechanic, such as:
<ul>
<li>As noted before, you will talk to yourself when alone and there will be narration about your actions in the third person</li>
<li>Whatever you named your PC as will be ignored and the character's default name will be displayed in the Party Talk screen. This is because the name is hard coded into the dialogue since the only character with a variable name (namely the PC) is not expected to talk, so your Marinaz will just be Marina. This does not rename you in anyway outside of the Party Talk window pop up.</li>
<li>There are some dialogues that you are prompted for a reaction or comment, like when O'saa is "whispering to himself", in which you will still get a prompt to ask what was it that he said and he will respond to you. So it's extra bizarre if you are playing as O'saa solo then you ask yourself what was it that you just whispered to yourself then you answer "nothing" back. Can't really fix this without overhauling how the Party Talk event is structured. Which I won't.</li>
<li>During the prologue when you get to the plank dimension you can use the Party Talk and you will end up seeing the same comment that your character would give when they revisit the place later in the game, which will be utter nonsense if this is your first time playing and might end up being a red herring about your character knowing what's up or not.</li>
</ul>

<h2>Install</h2>
This is a <b>Python script</b> so all you have to do is download the file, unzip it and then drop the <b>PCAPTscript.py</b> into the directory of: <br>
<code>Fear & Hunger 2 Termina/www/data</code>
<br>
Then just run the script with Python. In case you put it in the wrong folder it will tell you so in the terminal's window. 
<b>Note: Every time the game updates or you replace any Map files you will have to run this script again.</b>

<h2>Don’t have Python3 installed????</h2>
<a href="https://www.python.org/downloads/">Download it from the official website</a>
Then just make it so you run the <b>.py</b> file with Python.

<h2>Uninstall</h2>
To revert to the vanilla game just verify your steam game integrity cache and that will do it. If you're not on steam I sure hope you kept a backup of your <code>Fear & Hunger 2 Termina/www/data</code> directory, which you just copy and paste your backup into the game directory.

<h2>Compatibility</h2>
Because I am surgically altering each and every map file it should be completely compatible with any other mod that does not mess with Party Talk activation parameters. YES, it should even be compatible with mods that alter what is [b]actually said[/b], adds new dialogue, removes them, or whatnot. The only thing this script does is change the activation parameters for Party Talk that are [i]“Character is not the Player Character”[/i] to [i]“Character being in party”.[/i]
<br> <br>
<b>Another thing:</b> I made this with the foresight of Miro possibly adding EVERY single contestant as a playable character and even adding up to 20+ new locations (up to Map199) so this should stay compatible with most if not all future versions of the game provided that the Party Talk code isn’t fundamentally changed on how it is activated. You still have to re-run the script after every update, though, as it will likely overwrite the modified Map files.
