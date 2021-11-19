// also exported from '@storybook/react' if you can deal with breaking changes in 6.1
import { Meta, Story } from '@storybook/react/types-6-0';
import { MemoryRouter } from 'react-router';
import SideMenu from './SideMenu';

export default {
  title: 'Layouts/SideMenu',
  component: SideMenu,
  argTypes: {
  },
} as Meta;

const Template: Story = (args) => <MemoryRouter><SideMenu {...args}>{ }</SideMenu></MemoryRouter>;

export const Primary = Template.bind({});
Primary.args = {
};
