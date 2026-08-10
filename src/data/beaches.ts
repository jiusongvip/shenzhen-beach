export interface Beach {
  id: string;
  name: string;
  nameCN: string;
  distance: string;
  fee: string;
  feeNum: number;
  bestFor: string[];
  rating: number;
  crowdLevel: string;
  crowdLabel: string;
  location: [number, number];
  description: string;
  transport: Record<string, string | undefined>;
  facilities: Record<string, string | undefined>;
  features: Record<string, string>;
  tips: string[];
}

export const beaches: Beach[] = [];
export function getBeachById(id: string): Beach | undefined { return beaches.find(b => b.id === id); }