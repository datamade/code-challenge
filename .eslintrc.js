module.exports = {
  globals: {
    __PATH_PREFIX__: true,
  },
  extends: [
    "eslint:recommended",
    "plugin:prettier/recommended", // Add this line to use Prettier's recommended configuration
  ],
  plugins: ["prettier"], // Add this line to include the Prettier plugin
  rules: {
    "prettier/prettier": "error", // Add this line to show Prettier errors as ESLint errors
    indent: ["error", 2],
    "no-console": "off",
    strict: ["error", "global"],
    curly: "warn",
    semi: ["error", "never"],
    "space-in-parens": "off", // Turn off this rule
    "space-before-function-paren": "off", // Turn off this rule
    "space-before-blocks": ["error", "always"],
  },
  parserOptions: {
    ecmaVersion: 2020,
    sourceType: "module",
  },
  env: {
    browser: true,
    es6: true,
  },
};
