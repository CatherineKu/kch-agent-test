# Copyright (c) 2025 Beijing Volcano Engine Technology Co., Ltd. and/or its affiliates.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from veadk import Agent
from veadk.tools.builtin_tools.image_edit import image_edit
from veadk.tools.builtin_tools.video_generate import video_generate, video_task_query

INSTRUCTION_AGENT = """你是一个专业、可靠的智能助手。

你的目标是准确理解用户的需求，并给出条理清晰、简洁有用的回答。

约束：
- 信息不足时主动提问澄清，不要臆造事实。
- 需要时合理调用可用的工具，并说明关键结论。
- 保持礼貌、专业的语气。"""

INSTRUCTION_AGENT_SUB_1 = """你是一个专业、可靠的智能助手。

你的目标是准确理解用户的需求，并给出条理清晰、简洁有用的回答。

约束：
- 信息不足时主动提问澄清，不要臆造事实。
- 需要时合理调用可用的工具，并说明关键结论。
- 保持礼貌、专业的语气。"""

agent_sub_1 = Agent(
    name="kch_mvp_assisstant",
    description="一个基于 VeADK 构建的智能助手，理解用户意图并调用合适的工具完成任务。",
    instruction=INSTRUCTION_AGENT_SUB_1,
    tools=[image_edit, video_generate, video_task_query],
    model_name="doubao-seed-2-1-pro-260628",
)

agent = Agent(
    name="kch_test_mvp",
    description="一个基于 VeADK 构建的智能助手，理解用户意图并调用合适的工具完成任务。",
    instruction=INSTRUCTION_AGENT,
    model_name="doubao-seed-2-1-pro-260628",
    sub_agents=[agent_sub_1],
)

AGENT_DISPLAY_NAMES = {'kch_test_mvp': 'kch_test_mvp', 'kch_mvp_assisstant': 'kch_mvp_assisstant'}
AGENT_DRAFT = {'name': 'kch_test_mvp', 'description': '一个基于 VeADK 构建的智能助手，理解用户意图并调用合适的工具完成任务。', 'instruction': '你是一个专业、可靠的智能助手。\n\n你的目标是准确理解用户的需求，并给出条理清晰、简洁有用的回答。\n\n约束：\n- 信息不足时主动提问澄清，不要臆造事实。\n- 需要时合理调用可用的工具，并说明关键结论。\n- 保持礼貌、专业的语气。', 'agentType': 'llm', 'maxIterations': 3, 'a2aUrl': '', 'model': '', 'modelName': 'doubao-seed-2-1-pro-260628', 'modelProvider': '', 'modelApiBase': '', 'tools': [], 'skills': [], 'memory': {'shortTerm': False, 'longTerm': False}, 'knowledgebase': False, 'tracing': False, 'subAgents': [{'name': 'kch_mvp_assisstant', 'description': '一个基于 VeADK 构建的智能助手，理解用户意图并调用合适的工具完成任务。', 'instruction': '你是一个专业、可靠的智能助手。\n\n你的目标是准确理解用户的需求，并给出条理清晰、简洁有用的回答。\n\n约束：\n- 信息不足时主动提问澄清，不要臆造事实。\n- 需要时合理调用可用的工具，并说明关键结论。\n- 保持礼貌、专业的语气。', 'agentType': 'llm', 'maxIterations': 3, 'a2aUrl': '', 'model': '', 'modelName': 'doubao-seed-2-1-pro-260628', 'modelProvider': '', 'modelApiBase': '', 'tools': [], 'skills': [], 'memory': {'shortTerm': False, 'longTerm': False}, 'knowledgebase': False, 'tracing': False, 'subAgents': [], 'builtinTools': ['image_edit', 'video_generate'], 'customTools': [], 'mcpTools': [], 'a2aRegistry': {'enabled': False, 'registrySpaceId': '', 'registryTopK': '', 'registryRegion': '', 'registryEndpoint': ''}, 'shortTermBackend': 'local', 'longTermBackend': 'local', 'autoSaveSession': False, 'knowledgebaseBackend': 'viking', 'knowledgebaseIndex': '', 'tracingExporters': [], 'selectedSkills': [], 'workflow': None, 'deployment': {'feishuEnabled': False, 'envValues': {}}}], 'builtinTools': [], 'customTools': [], 'mcpTools': [], 'a2aRegistry': {'enabled': False, 'registrySpaceId': '', 'registryTopK': '', 'registryRegion': '', 'registryEndpoint': ''}, 'shortTermBackend': 'local', 'longTermBackend': 'local', 'autoSaveSession': False, 'knowledgebaseBackend': 'viking', 'knowledgebaseIndex': '', 'tracingExporters': [], 'selectedSkills': [], 'workflow': None, 'deployment': {'feishuEnabled': False, 'envValues': {}}}

# ADK 加载器要求：顶层 agent 必须命名为 root_agent
root_agent = agent
