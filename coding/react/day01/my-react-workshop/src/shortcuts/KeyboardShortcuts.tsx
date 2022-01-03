import useMousetrap from '../hooks/use-mousetrap';
import { useNavigate } from 'react-router-dom';

function KeyboardShortcuts() {
  const navigate = useNavigate()

  // shortcuts
  useMousetrap("g h", () => navigate("/"));
  useMousetrap("g m", () => navigate("/movies"));
  useMousetrap("g a", () => navigate("/about"));

  return <></>
}

export default KeyboardShortcuts
