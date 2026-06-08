import { useState, useEffect } from 'react';

export function usePulse(intervalMs: number = 2000) {
  const [pulse, setPulse] = useState(false);

  useEffect(() => {
    const interval = setInterval(() => {
      setPulse(true);
      setTimeout(() => setPulse(false), intervalMs / 2);
    }, intervalMs);
    return () => clearInterval(interval);
  }, [intervalMs]);

  return pulse;
}
