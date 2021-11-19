# Day 2

During this day we setup storybook and add basic UI components.

## Setup Storybook

We use `@next` version and a specific builder to leverage vite for hot reload.

```sh
npx sb@next init --builder storybook-builder-vite
```

Tailwind uses PostCSS8 and for Storybook to support it we can use [@storybookjs/addon-postcss](https://github.com/storybookjs/addon-postcss)

```sh
yarn add -D @storybook/addon-postcss
```

within `.storybook/main.js`:

```js
module.exports = {
  addons: [
    {
      name: '@storybook/addon-postcss',
      options: {
        postcssLoaderOptions: {
          implementation: require('postcss'),
        },
      },
    },
  ],
};
```