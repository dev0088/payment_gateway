const REQUEST = 'REQUEST';
const SUCCESS = 'SUCCESS';
const FAILURE = 'FAILURE';
const RECEIVED = 'RECEIVED';
const INIT = 'INIT';

const createRequestTypes = base => {
  const res = {};
  const subTypes = [REQUEST, SUCCESS, FAILURE, RECEIVED, INIT];
  subTypes.forEach(type => {
    res[type] = `${base}_${type}`;
  });
  return res;
};

export const LOGIN = createRequestTypes('LOGIN');
export const TOKEN = createRequestTypes('TOKEN');
export const REGISTER = createRequestTypes('REGISTER');
export const LOGOUT = createRequestTypes('LOGOUT');
export const GET_PROFILE = createRequestTypes('GET_PROFILE');
export const GET_CONTACTS = createRequestTypes('GET_CONTACTS');
export const GET_CALENDAR_EVENTS = createRequestTypes('GET_CALENDAR_EVENTS');
