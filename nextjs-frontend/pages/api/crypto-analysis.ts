import { NextApiRequest, NextApiResponse } from 'next';
import axios from 'axios';

const BACKEND_URL = 'http://localhost:8000';

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  try {
    const response = await axios.get(`${BACKEND_URL}/api/crypto-analysis`);
    res.status(200).json(response.data);
  } catch (error) {
    console.error('Error fetching crypto analysis:', error);
    res.status(500).json({ error: 'Failed to fetch crypto analysis' });
  }
}