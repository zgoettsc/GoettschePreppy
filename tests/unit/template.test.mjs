import test from 'node:test';
import assert from 'node:assert/strict';
import { render, parse, TemplateError, BLANK_HTML, formatValue } from '../../app/lib/template.js';

const ctx = {
  household: { size: 3, name: 'Our household' },
  home: { county: 'Cook County', town: null },
  has: { pool: true, well: false, condition: { 'CL-01': true } },
  members: [{ label: 'Ann', conditions: ['Asthma (CL-07)', 'Food allergy (CL-04)'] }, { label: 'Bo', conditions: [] }],
  pets: [],
  destinations: [{ name: 'Cabin', region: { state_name: 'Iowa', zone: '5a' } }],
  derived: { water: { two_weeks_gal: 55 }, calories: { two_weeks: 84000 } },
};

test('values, blanks and escaping', () => {
  assert.equal(render('Size {{ household.size }}.', ctx), 'Size 3.');
  assert.equal(render('Town {{home.town}}.', ctx), `Town ${BLANK_HTML}.`);
  assert.equal(render('{{ nope.path }}', ctx), BLANK_HTML);
  const blanks = [];
  render('{{ home.town }} {{ home.county }}', ctx, { onBlank: p => blanks.push(p) });
  assert.deepEqual(blanks, ['home.town']);
  assert.equal(render('{{ x }}', { x: 'a*b|c <i>' }), 'a&#42;b&#124;c &#60;i&#62;');
  assert.equal(render('{{ x }}', { x: '' }), BLANK_HTML);
  assert.equal(render('{{ x }}', { x: [] }), BLANK_HTML);
});

test('formatting block of schema/context.json', () => {
  assert.equal(formatValue(true), 'yes');
  assert.equal(formatValue(false), 'no');
  assert.equal(formatValue(84000), '84,000');
  assert.equal(formatValue(1234.5), '1,234.5');
  assert.equal(formatValue(['a']), 'a');
  assert.equal(formatValue(['a', 'b', 'c']), 'a, b and c');
  assert.equal(formatValue(0), '0');
  assert.equal(formatValue(null), null);
  assert.equal(render('{{ derived.calories.two_weeks }}', ctx), '84,000');
});

test('#if, !flag, else, nesting', () => {
  assert.equal(render('{{#if has.pool}}P{{else}}N{{/if}}', ctx), 'P');
  assert.equal(render('{{#if has.well}}W{{else}}N{{/if}}', ctx), 'N');
  assert.equal(render('{{#if !has.well}}no well{{/if}}', ctx), 'no well');
  assert.equal(render('{{#if has.pool}}a{{#if has.well}}b{{else}}c{{/if}}d{{/if}}', ctx), 'acd');
  assert.equal(render('{{#if has.condition.CL-01}}T1D{{/if}}', ctx), 'T1D');
  assert.equal(render('{{#if has.unknown}}x{{else}}y{{/if}}', ctx), 'y');
});

test('#each with fields, else, loop scope over context', () => {
  assert.equal(render('{{#each members as m}}[{{m.label}}]{{/each}}', ctx), '[Ann][Bo]');
  assert.equal(render('{{#each pets as p}}x{{else}}none{{/each}}', ctx), 'none');
  assert.equal(render('{{#each destinations as d}}{{d.name}} {{d.region.zone}} {{household.size}}{{/each}}', ctx), 'Cabin 5a 3');
  assert.equal(render('{{#each members as m}}{{m.conditions}};{{/each}}', ctx), `Asthma (CL-07) and Food allergy (CL-04);${BLANK_HTML};`);
});

test('standalone block tags remove their line', () => {
  const src = '| a | b |\n|---|---|\n{{#each members as m}}\n| {{m.label}} | x |\n{{/each}}\nend';
  assert.equal(render(src, ctx), '| a | b |\n|---|---|\n| Ann | x |\n| Bo | x |\nend');
  const list = '- one\n  {{#if has.well}}\n- well\n  {{/if}}\n- two';
  assert.equal(render(list, ctx), '- one\n- two');
});

test('special forms go to hooks', () => {
  const hooks = { choice: id => `<${id}>`, card: id => `[${id}]`, photo: id => `(p:${id})`, figure: id => `(f:${id})`, plates: () => '(plates)', ai: id => `(ai:${id})` };
  assert.equal(render('{{choice DC-01}} {{card DC-02}} {{photo warm-room}} {{figure fig-a}} {{plates}} {{ai x-y}}', ctx, hooks),
    '<DC-01> [DC-02] (p:warm-room) (f:fig-a) (plates) (ai:x-y)');
});

test('errors', () => {
  assert.throws(() => parse('{{#if a}}x'), TemplateError);
  assert.throws(() => parse('{{/if}}'), TemplateError);
  assert.throws(() => parse('{{#each a as b}}{{/if}}'), TemplateError);
  assert.throws(() => parse('{{ a + b }}'), TemplateError);
  assert.throws(() => parse('{{else}}'), TemplateError);
});
