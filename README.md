# specialhugband.com

the special hug website. plain html and css, no build step, no javascript. geocities energy on purpose.

## files

- `index.html` the whole site. every section is in here.
- `style.css` colors, fonts, layout. colors are the lines at the top.
- `img/photo-1.jpg` ... `photo-6.jpg` the six photos on the home page (square, 800px).
- `img/` everything else in here (wordmark, headings, 88x31 buttons, sparkles, divider, new! badge, under construction, counter, starry background) is pixel art drawn by `make-gfx.py`.
- `make-gfx.py` draws all of the above. edit a word or a color in it, run `python3 make-gfx.py` from this folder (needs pillow: `pip install pillow`), and the graphics regenerate. you do not need to run it unless you change something.
- `CNAME` tells github pages which domain this is. do not delete. held back by `.gitignore` until launch, see below.
- `.nojekyll` tells github pages to serve the files as-is. do not delete.
- `make-placeholders.py` and `img/paper.png` are leftovers from the first version. safe to delete.

## how to update

### new song out? update the hero

the box at the top is the latest release. when a new song drops: save its cover over `img/severance.jpg` (or a new file, and change the `src`), change the word `severance` in `make-gfx.py` and run it so the pixel title updates, then swap the four listen links, the video link, and the alt text. all marked with a comment in `index.html`. also update the scrolling banner.

### add or remove a show

open `index.html`, find `<ul class="shows">`. each show is one `<li> ... </li>` block:

```html
<li>
  <time datetime="2026-09-10T21:30">thu sept 10, 2026</time>
  <span class="where">the meatlocker, 8 park st, montclair nj</span>
  <span class="details">doors 9pm, show 9:30pm, $15 at the door</span>
  <span class="with">w/ polaroids, starlily, falling into light</span>
</li>
```

copy a block, paste it under the last one, change the words. delete a block to remove a show. if there are no shows, delete all the blocks and leave the "new shows get posted here" line.

### swap a photo

save your photo over `img/photo-3.jpg` (or whichever slot). keep the same file name. square, under 150 kb is ideal. on a mac: open the photo in preview, tools, adjust size, width 1000, then file, export, jpeg, quality around 60.

then in `index.html` change that image's `alt="..."` to a short description of the new photo, like `alt="faith singing with eyes closed at ottobar"`. that is what screen readers say.

### change the bio, links, email, scrolling banner

all in `index.html`. search for the text you want to change. the scrolling banner text is the `<p class="marquee">` line near the top.

### the blinking new! badge

it is the `<img class="new" ...>` line inside a show. move it to whichever show is newest, or delete the line.

### the visitor counter

it is a picture (`img/counter.png`) that says 00000001. it does not count anything. that is the joke. if you ever want a real one, it needs a third party service, so ask before adding.

### mailing list

the signup box is a plain `<form>` in the contact section. right now its `action` is a `mailto:` to the band email, so "sign me up" opens the visitor's email app with their address in the body and they hit send. no service, no cost, a little clunky, and it does nothing for people without a mail app set up. when you pick a real provider (buttondown, mailchimp, etc.), paste its form url into `action=""`, rename the input if the provider wants a different `name`, and delete the fine-print line.

### merch

its own section: one big button (`img/btn-merch.png`, drawn by `make-gfx.py`) linking to the bandcamp merch page.

## editing and publishing (github pages)

the code lives in a github repo, `xignoe/specialhugband`. github pages serves it. pushing to `main` publishes within about a minute.

- preview (now): https://xignoe.github.io/specialhugband/
- live (later): https://specialhugband.com

### going live on specialhugband.com

the `CNAME` file is in this folder but held back by `.gitignore` so the preview works on the github.io address first. when the band says go:

1. delete the `CNAME` line from `.gitignore`, commit, push.
2. repo settings, pages. under "custom domain" type `specialhugband.com`, save.
3. faith adds dns records where the domain was bought (namecheap, godaddy, google, wherever):
   - four `A` records for host `@` pointing to `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - one `CNAME` record for host `www` pointing to `xignoe.github.io`
   these are github's published addresses. if they ever change, github's docs page "managing a custom domain for your github pages site" has the current ones.
4. wait up to an hour for dns. back in pages settings, tick "enforce https" once it lets you.

### everyday edits

1. open the repo on github.com, click `index.html`, click the pencil icon.
2. make the change, scroll down, "commit changes".
3. refresh the site in about a minute.

for photos: in the repo click the `img` folder, "add file", "upload files", drop the new `photo-N.jpg` on it. it replaces the old one with the same name.

or, from this folder in terminal: `git add -A && git commit -m "what changed" && git push`.

### comments from the band

open an issue on the repo (issues tab, new issue) or just text kevin.

## rules of the house

- everything lowercase.
- no em-dashes.
- no trackers, no cookie banners, no ads, no javascript unless there is a very good reason.
- one file per thing. do not add a framework.
- every graphic is drawn by `make-gfx.py`, not downloaded. keep it that way, it is the whole point.
