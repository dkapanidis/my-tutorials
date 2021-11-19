# Day 1

During this day we setup the react app, install [Tailwind CSS], configure page navigation and prepare a side menu with tooltips and keyboard shortcuts. Once finished we prepare an ARCHITECTURE.md that describes in high-level the system.

[Tailwind CSS]:https://tailwindcss.com/

### Setup React App

To bootstrap the project we'll use [create-react-app]

[create-react-app]:https://github.com/facebook/create-react-app

```sh
yarn create react-app my-react-workshop --template typescript
cd my-react-workshop
```

Start app

```sh
yarn start
```

### Setup Vite

We'll use [vite] as build tool.

Install packages

```sh
yarn add -D vite @vitejs/plugin-react-refresh
```

Create a vite config file: `vite.config.ts`

```ts
// vite.config.ts
import { defineConfig } from 'vite'
import reactRefresh from '@vitejs/plugin-react-refresh'

export default defineConfig({
  plugins: [reactRefresh()]
})
```

Edit `package.json`

```sh
// package.json
{
  "scripts": {
    "start": "vite",
    "build": "vite build"
  },
}
```

Move index.html from /public to your project root and remove all %PUBLIC_URL%, and add a `<script>` tag to reference `/src/index.tsx`.

```diff
<!-- index.tsx -->

<!-- before -->
- <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
- <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
- <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />

<!-- after -->
+ <link rel="icon" href="/favicon.ico" />
+ <link rel="apple-touch-icon" href="/logo192.png" />
+ <link rel="manifest" href="/manifest.json" />

  <div id="root"></div>
+ <script type="module" src="/src/index.tsx"></script>
```

Start app

```sh
yarn start
```

### Setup Tailwind CSS

We'll use [Tailwind CSS] as a utility-first CSS framework.
