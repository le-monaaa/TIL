console.log("sw-omnibox.js")

// Save default API suggestions
// 확장프로그램 처음 설치되는 시점에
// runtime.onInstalled() 이벤트 수신 대기하여 상태 초기화
chrome.runtime.onInstalled.addListener(({ reason }) => {
    if (reason === 'install') {
      chrome.storage.local.set({
        apiSuggestions: ['tabs', 'storage', 'scripting']
      });
    }
  });

const URL_CHROME_EXTENSIONS_DOC =
    'https://developer.chrome.com/docs/extensions/reference/';
const NUMBER_OF_PREVIOUS_SEARCHES = 4;

// Display the suggestions after user starts typing
chrome.omnibox.onInputChanged.addListener(async (input, suggest) => {
  await chrome.omnibox.setDefaultSuggestion({
    description: 'Enter a Chrome API or choose from past searches'
  });
  const { apiSuggestions } = await chrome.storage.local.get('apiSuggestions');
  const suggestions = apiSuggestions.map((api) => {
    return { content: api, description: `Open chrome.${api} API` };
  });
  suggest(suggestions);
});

// Open the reference page of the chosen API
// 사용자가 추천 항목을 선택하면 onInputEntered()에서 해당 Chrome API 참조 페이지를 엽니다.
chrome.omnibox.onInputEntered.addListener((input) => {
    chrome.tabs.create({ url: URL_CHROME_EXTENSIONS_DOC + input });
    // Save the latest keyword
    updateHistory(input);
  });

  //updateHistory() 함수는 검색주소창 입력을 받아 storage.local에 저장합니다. 
  // 이렇게 하면 가장 최근 검색어를 나중에 검색주소창 추천으로 사용할 수 있습니다.

  async function updateHistory(input) {
    const { apiSuggestions } = await chrome.storage.local.get('apiSuggestions');
    apiSuggestions.unshift(input);
    apiSuggestions.splice(NUMBER_OF_PREVIOUS_SEARCHES);
    return chrome.storage.local.set({ apiSuggestions });
  }

  