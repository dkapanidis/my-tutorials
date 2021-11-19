import { addDecorator } from '@storybook/react';
import React from 'react';
import { MemoryRouter } from 'react-router-dom';
import '../src/index.css';
import '../src/App.css';

// addDecorator(storyFn => <div>{storyFn()}</div>)
// addDecorator(storyFn => <MemoryRouter>  {storyFn()}</MemoryRouter>)

export const parameters = {
  actions: { argTypesRegex: "^on[A-Z].*" },
  controls: {
    matchers: {
      color: /(background|color)$/i,
      date: /Date$/,
    },
  },
}