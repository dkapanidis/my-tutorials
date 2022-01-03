import { MemoryRouter } from 'react-router-dom';
import '../src/index.css';
import '../src/App.css';

const Layout = ({ children }) => {
  return (
    <MemoryRouter>
      {children}
    </MemoryRouter>
  )
}

export default Layout;
