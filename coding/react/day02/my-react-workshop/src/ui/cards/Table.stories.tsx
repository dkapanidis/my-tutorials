// also exported from '@storybook/react' if you can deal with breaking changes in 6.1
import { Meta, Story } from '@storybook/react/types-6-0';
import { MemoryRouter } from 'react-router';
import Table, { Props } from './Table';

export default {
  title: 'Cards/Table',
  component: Table,
  argTypes: {
  },
} as Meta;

const Template: Story<Props> = (args: Props) => <MemoryRouter>
  <Table {...args} />
</MemoryRouter>

export const Primary = Template.bind({});
Primary.args = {
  to: "/movies/view",
  columns: ["id", "title"],
  items: [
    { id: 1, title: "hello" },
    { id: 2, title: "second item" }
  ]
};
