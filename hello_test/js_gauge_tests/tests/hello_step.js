/* globals gauge*/
"use strict";
const assert = require("assert");

step("有 <content>", (content) => {
    assert.equal(content, "getgauge/taiko", "content错误")
});