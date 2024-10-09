import { createClient } from 'redis';

async function subscriber() {
  const client = createClient();

  client.on('error', (err) => console.log('Redis client not connected to the server:', err));

  await client.connect();
  console.log('Redis connected to the server');

  await client.subscribe('holberton school channel', async (message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
      await client.unsubscribe();
      await client.quit()
    }
  });
}

subscriber();
