// also exported from '@storybook/react' if you can deal with breaking changes in 6.1
import { Meta, Story } from '@storybook/react/types-6-0';
import Card from './Card';

export default {
  title: 'Cards/Card',
  component: Card,
  argTypes: {
  },
} as Meta;

export const Primary: Story = () => <div className="h-96">
  <Card>
  <div className="w-full h-full bg-green-200" />
</Card>
</div>
export const VerticalScroll: Story = () => <Card>
  <div className="w-full py-10 bg-green-200" />
  <div className="w-full py-10 bg-blue-200" />
  <div className="w-full py-10 bg-green-200" />
  <div className="w-full py-10 bg-blue-200" />
  <div className="w-full py-10 bg-green-200" />
  <div className="w-full py-10 bg-blue-200" />
  <div className="w-full py-10 bg-green-200" />
  <div className="w-full py-10 bg-blue-200" />
  <div className="w-full py-10 bg-green-200" />
</Card>
