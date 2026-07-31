import sharp from "sharp";
import path from "node:path";
import { mkdir, access } from "node:fs/promises";
import { constants } from "node:fs";

const projectRoot = process.cwd();

const source = path.join(projectRoot, "assets", "master-icon.png");
const output = path.join(projectRoot, "public");

const icons = [
  ["icon-192.png", 192],
  ["icon-512.png", 512],
  ["apple-touch-icon.png", 180],
  ["favicon-32.png", 32],
  ["favicon-16.png", 16],
];

async function exists(file) {
  try {
    await access(file, constants.F_OK);
    return true;
  } catch {
    return false;
  }
}

async function generate() {
  if (!(await exists(source))) {
    console.error("❌ master-icon.png not found.");
    console.error(`Expected:\n${source}`);
    process.exit(1);
  }

  await mkdir(output, { recursive: true });

  for (const [name, size] of icons) {
    await sharp(source)
      .resize(size, size)
      .png()
      .toFile(path.join(output, name));

    console.log(`✓ ${name}`);
  }

  console.log("\n🎉 Icons generated successfully.");
}

generate().catch(console.error);