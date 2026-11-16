# ai blocks: how to write a spec

An ai block is the only place where the generation model writes prose into a binder. A household
page (`layer: household`, nowhere else) inserts `{{ai block-id}}`, and the spec for it lives here
as `content/ai-blocks/<block-id>.md`. Everything else in the binder is template text written by
people and filled from the profile. Use an ai block only for prose that cannot be templated: a
paragraph that has to weigh several of the household's answers together (a destination's honest
read, who must know which life-sustaining routine).

The model sees: the kit's fixed rules (below), every spec in this folder (one cached system prompt,
the same for every household), the page title, and the **inputs** this spec names, read from the
household's context (`schema/context.json`). It sees nothing else of the profile.

## File format

```markdown
# ai block: <block-id>

- **Used on:** `NN-MM-slug` (household layer), where on the page.
- **Written by:** <worker id>, <date>.

## Purpose
Why this needs prose, in two to four sentences.

## Inputs (exact context paths; nothing else)
- `list[]`: `field`, `field`, and from its `region`: `field`, `field`
- `path.to.value`, `has.flag`, `has.condition.CL-NN`
- `list[]`: `field`, `field` (do **not** use `other_field`)

## Output
The shape: Markdown paragraphs or a bullet list, what each covers and in what order, and the exact
sentence to print when the inputs are empty.

## Constraints
What it must never do beyond the fixed rules (see below).

## Length
Hard limits: words per paragraph or bullet, number of paragraphs or bullets.

## Example shape (illustrative only; never copy)
A short example with made-up values.
```

### The Inputs section is machine-read

`scripts/build-kit.mjs` reads the `## Inputs` section, bullet by bullet, and only the backticked
names in it:

- A bullet whose **first** backticked name is `list[]` (for example `destinations[]`, `members[]`,
  `meds[]`) passes that list to the model, keeping only the backticked field names that follow.
  After the word `` `region` `` the names are fields of each item's region object.
  Without field names, the whole list item is passed.
- Any other backticked name that is a context path (`household.size`, `region.home.hazards`,
  `has.anaphylaxis`) is passed as that value. `has.condition.CL-NN` passes all condition flags.
- Names inside a parenthesis that contains the word "not" are **excluded**:
  `(do **not** use `strength` or `schedule`)`.
- Anything else in backticks (page ids like `02-NN`, example text) is ignored.
- The selected condition modules are always passed as `condition_pages` (name and `02-NN` page),
  so a block can point to them.

Check what build-kit read: `node -e 'console.log(JSON.stringify(require("./app/build/kit.json").ai_blocks["<id>"].inputs))'`.
A spec may instead give `inputs:` as YAML front matter (a list of paths and
`{ list, fields, region }` objects); front matter wins over the section.

## Fixed rules for every block (the model is told these; the generator enforces the first two)

1. **The model may not introduce a number, phone number, web address, law, regulation, dose or
   procedure that is not in its inputs.** After the model answers, the generator compares every
   number in the text with the numbers in the inputs (cross-references written `→ NN-MM` are
   exempt). A block that adds one is thrown away, the slot prints a fill-in blank, and the Review
   notes page says so. Laws and procedures are checked by the review pass.
2. No web address and no "look it up online". No template braces in the output.
3. Plain words for someone who has never prepared; short sentences; calm, direct; the binder's
   voice. Markdown body text only: no title, no front matter, no preamble.
4. Never present an option from a decision card as the household's rule unless the inputs carry
   that choice; never relax a floor (`docs/05-decision-cards.md` part B).
5. Stay within the spec's length.

The block is shown in the binder inside a frame labelled "Written by the AI from your answers".

## Writing a good spec

- Name the fewest inputs that do the job. Every field you pass is something the model can repeat;
  do not pass free text you do not want quoted (prescriber instructions, phone numbers).
- Say exactly what to print when the inputs are empty or a value is missing.
- Give the order of the content, not just the topics.
- Cross-references the block may use go in the Output section as `→ NN-MM`.
- Keep it short: a block is one or a few paragraphs, never a page.
