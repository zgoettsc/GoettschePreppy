// Cloudflare Worker entry point for the GoettschePreppy relay.
// All logic lives in ./relay.js. This module exports only the default handler:
// the Workers runtime treats every named export of the entry module as an
// entrypoint, so constants and helpers must not be exported from here.
import { makeHandler } from "./relay.js";

const handler = makeHandler();

export default {
  fetch(request, env, ctx) {
    return handler(request, env, ctx);
  },
};
