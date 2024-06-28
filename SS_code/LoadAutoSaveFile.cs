private void LoadAutoSaveFile(string t)
{
	GC.Collect();
	string[] array = this.ReadTblLine(t);
	int num = -1;
	int num2 = -1;
	int num3 = -1;
	int num4 = -1;
	int num5 = -1;
	int num6 = -1;
	int num7 = -1;
	int num8 = -1;
	int num9 = -1;
	int num10 = -1;
	int num11 = -1;
	int num12 = -1;
	int num13 = -1;
	int num14 = -1;
	for (int i = 0; i < array.Length; i++)
	{
		if (array[i].Contains("TrainCnt:"))
		{
			num = i;
		}
		else if (array[i].Contains("RailPos0:"))
		{
			num2 = i;
		}
		else if (array[i].Contains("RailPos1:"))
		{
			num3 = i;
		}
		else if (array[i].Contains("Speed0:"))
		{
			num4 = i;
		}
		else if (array[i].Contains("Speed1:"))
		{
			num5 = i;
		}
		else if (array[i].Contains("Dir0:"))
		{
			num13 = i;
		}
		else if (array[i].Contains("Dir1:"))
		{
			num14 = i;
		}
		else if (array[i].Contains("CPU:"))
		{
			num6 = i;
		}
		else if (array[i].Contains("CPUParam:"))
		{
			num7 = i;
		}
		else if (array[i].Contains("ComicScript:"))
		{
			num8 = i;
		}
		else if (array[i].Contains("CPUEvent:"))
		{
			num9 = i;
		}
		else if (array[i].Contains("RainEvent:"))
		{
			num10 = i;
		}
		else if (array[i].Contains("RailCnt:"))
		{
			num11 = i;
		}
		else if (array[i].Contains("AmbCnt:"))
		{
			num12 = i;
		}
	}
	string[] array13 = this.ReadTbl(array[num]);
	string[] array2 = this.ReadTbl(array[num2]);
	string[] array3 = null;
	if (num3 > 0)
	{
		array3 = this.ReadTbl(array[num3]);
	}
	string[] array4 = this.ReadTbl(array[num4]);
	string[] array5 = null;
	if (num5 > 0)
	{
		array5 = this.ReadTbl(array[num5]);
	}
	string[] array6 = null;
	if (num6 > 0)
	{
		array6 = this.ReadTbl(array[num6]);
	}
	string[] array7 = null;
	if (num7 > 0)
	{
		array7 = this.ReadTbl(array[num7]);
	}
	string[] array8 = this.ReadTbl(array[num8]);
	string[] array9 = null;
	if (num9 > 0)
	{
		array9 = this.ReadTbl(array[num9]);
	}
	string[] array10 = null;
	if (num10 > 0)
	{
		array10 = this.ReadTbl(array[num10]);
	}
	int num15 = int.Parse(array13[1]);
	if (num11 > 0)
	{
		int num16 = int.Parse(this.ReadTbl(array[num11])[1]);
		if (num16 == SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.RailList.Length)
		{
			for (int j = 0; j < num16; j++)
			{
				string[] array11 = this.ReadTbl(array[num11 + 1 + j]);
				rail_list rail_list = SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.RailList[j];
				int num17 = 1;
				rail_list.prev_rail = int.Parse(array11[num17++]);
				rail_list.block = int.Parse(array11[num17++]);
				float x = float.Parse(array11[num17++]);
				float y = float.Parse(array11[num17++]);
				float z = float.Parse(array11[num17++]);
				rail_list.offsetpos = new Vector3(x, y, z);
				float x2 = float.Parse(array11[num17++]);
				float y2 = float.Parse(array11[num17++]);
				float z2 = float.Parse(array11[num17++]);
				rail_list.dir = new Vector3(x2, y2, z2);
				rail_list.mdl_no = int.Parse(array11[num17++]);
				rail_list.kasenchu_mdl_no = int.Parse(array11[num17++]);
				rail_list.per = float.Parse(array11[num17++]);
				byte flg = byte.Parse(array11[num17++]);
				byte flg2 = byte.Parse(array11[num17++]);
				byte flg3 = byte.Parse(array11[num17++]);
				byte flg4 = byte.Parse(array11[num17++]);
				rail_list.flg = Define.Flg(flg, flg2, flg3, flg4);
				int num18 = int.Parse(array11[num17++]);
				for (int k = 0; k < num18; k++)
				{
					rail_list.r[k].next.rail = int.Parse(array11[num17++]);
					rail_list.r[k].next.no = int.Parse(array11[num17++]);
					rail_list.r[k].prev.rail = int.Parse(array11[num17++]);
					rail_list.r[k].prev.no = int.Parse(array11[num17++]);
				}
			}
			int num19 = 31;
			ulong num20 = 1UL << (num19 & 31);
			for (int l = 0; l < num16; l++)
			{
				rail_list rail_list2 = SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.RailList[l];
				if (rail_list2.block < 0 || rail_list2.block >= this.mRailMgr.BlockList.Count)
				{
					Debug.LogError("r.block Err!!:" + l);
				}
				int mdl_no = rail_list2.mdl_no;
				if (mdl_no < 0 || mdl_no >= SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.MdlList.Length)
				{
					Debug.LogError(string.Concat(new object[]
					{
						"CreateStage mdl_no Err!!:",
						l,
						" ",
						mdl_no
					}));
					break;
				}
				Rail rail = this.mRailMgr.RailList[l];
				if (rail == null)
				{
					Debug.LogError("rail Err!!");
				}
				else
				{
					this.mRailMgr.SetUpRail(SingletonMonoBehaviour<cGameMgr>.Instance.mMdlMgr, rail, l, mdl_no, rail_list2);
				}
				if (((ulong)SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.RailList[l].flg & num20) > 0UL)
				{
					rail.BlockNo = -1;
					rail.gameObject.SetActive(false);
				}
			}
			this.mRailMgr.AllInit = false;
			for (int m = 0; m < this.mRailMgr.RailList.Count; m++)
			{
				this.mRailMgr.RailList[m].InitFlg = true;
				this.mRailMgr.RailList[m].InitPosFlg = false;
			}
			for (int n = 0; n < this.mRailMgr.RailList.Count; n++)
			{
				this.mRailMgr.Init(n, null);
			}
			this.mRailMgr.AllInit = true;
			for (int num21 = 0; num21 < this.mRailMgr.RailList.Count; num21++)
			{
				if (!(this.mRailMgr.RailList[num21] == null) && !this.mRailMgr.RailList[num21].mRailFlg.ChkFlg(31))
				{
					this.mRailMgr.RailList[num21].MathLength();
				}
				if (!(this.mRailMgr.RailList[num21] == null) && !this.mRailMgr.RailList[num21].mRailFlg.ChkFlg(31))
				{
					this.mRailMgr.UpdateRail(num21);
				}
			}
			List<Rail> list = this.mRailMgr.ChkNullRail(false, true);
			if (list != null)
			{
				this.mRailMgr.NullRailRec(list);
			}
		}
	}
	if (num12 > 0)
	{
		int num22 = int.Parse(this.ReadTbl(array[num12])[1]);
		int num23 = int.Parse(this.ReadTbl(array[num12])[2]);
		if (num22 == SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.AmbList.Length)
		{
			for (int num24 = 0; num24 < num22; num24++)
			{
				string[] array12 = this.ReadTbl(array[num12 + 1 + num24]);
				amb_list amb_list = SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.AmbList[num24];
				int num25 = 1;
				amb_list.rail_no = int.Parse(array12[num25++]);
				amb_list.length = float.Parse(array12[num25++]);
				int num26 = int.Parse(array12[num25++]);
				amb_list.datalist.Clear();
				for (int num27 = 0; num27 < num26; num27++)
				{
					amb_data amb_data = new amb_data();
					amb_data.mdl_no = int.Parse(array12[num25++]);
					amb_data.parentindex = int.Parse(array12[num25++]);
					float x3 = float.Parse(array12[num25++]);
					float y3 = float.Parse(array12[num25++]);
					float z3 = float.Parse(array12[num25++]);
					amb_data.offsetpos = new Vector3(x3, y3, z3);
					float x4 = float.Parse(array12[num25++]);
					float y4 = float.Parse(array12[num25++]);
					float z4 = float.Parse(array12[num25++]);
					amb_data.dir = new Vector3(x4, y4, z4);
					float x5 = float.Parse(array12[num25++]);
					float y5 = float.Parse(array12[num25++]);
					float z5 = float.Parse(array12[num25++]);
					amb_data.joint_dir = new Vector3(x5, y5, z5);
					amb_data.per = float.Parse(array12[num25++]);
					if (num23 >= 1 && array12.Length > num25)
					{
						amb_data.size_per = float.Parse(array12[num25++]);
					}
					else
					{
						amb_data.size_per = 1f;
					}
					amb_list.datalist.Add(amb_data);
				}
			}
			this.mAmbMgr.DeleteAmbList();
			for (int num28 = 0; num28 < SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.AmbList.Length; num28++)
			{
				int parentAmbNo = num28;
				if (SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.AmbList[num28] == null)
				{
					Debug.LogError("cGameMgr.Instance.mStageTblMgr.AmbList Null!!" + num28);
				}
				else if (SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.AmbList[num28].rail_no < 0)
				{
					Debug.LogError("AMB" + num28 + " NoCreate!");
				}
				else
				{
					for (int num29 = 0; num29 < SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.AmbList[num28].datalist.Count; num29++)
					{
						int mdl_no2 = SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.AmbList[num28].datalist[num29].mdl_no;
						if (mdl_no2 < 0 || mdl_no2 >= this.mMdlMgr.MdlList.Count)
						{
							Debug.LogError(string.Concat(new object[]
							{
								"CreateStage AmbMdl_no Err!!:",
								num28,
								" ",
								mdl_no2
							}));
							break;
						}
						amb_data amb_data2 = SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.AmbList[num28].datalist[num29];
						GameObject gameObject = this.mMdlMgr.MdlCreate(mdl_no2, false, this.mRailMgr.BlockTree);
						if (gameObject != null)
						{
							AmbObj component = gameObject.GetComponent<AmbObj>();
							if (component != null)
							{
								if (num29 == 0)
								{
									component.ParentRailNo = SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.AmbList[num28].rail_no;
									component.ParentAmbNo = parentAmbNo;
									component.ParentAmbIndex = -1;
									if (component.ParentRailNo >= 0 && component.ParentRailNo < this.mRailMgr.RailList.Count)
									{
										SingletonMonoBehaviour<cGameMgr>.Instance.InitTransform(this.mRailMgr.RailList[component.ParentRailNo].transform, component.transform);
									}
								}
								else
								{
									component.transform.parent = base.transform;
									component.ParentRailNo = -1;
									component.ParentAmbNo = parentAmbNo;
									component.ParentAmbIndex = num29 - 1;
								}
								component.MdlNo = mdl_no2;
								component.ParentAmbIndex = amb_data2.parentindex;
								component.BasePos = amb_data2.offsetpos;
								component.BaseRot = amb_data2.dir;
								component.JointDir = amb_data2.joint_dir;
								component.LengthPer = amb_data2.per;
								component.KasenChuScale = amb_data2.size_per;
								if (component.mKasenChu != null)
								{
									component.mKasenChu.SetScale(component.KasenChuScale);
								}
								component.GetKoukoku();
								component.GetSkinnedMeshRenderer();
								component.ReBounds();
								this.mAmbMgr.AmbList.Add(component);
							}
							else
							{
								Debug.LogError("amb_obj Err!!");
								Debug.LogError(string.Concat(new string[]
								{
									num28.ToString(),
									", ",
									num29.ToString(),
									", ",
									mdl_no2.ToString()
								}));
							}
						}
					}
				}
			}
			this.mAmbMgr.UpdateAll();
		}
	}
	int r = int.Parse(array2[1]);
	int no = int.Parse(array2[2]);
	float setRailPos = float.Parse(array2[3]);
	RailLine railLine = this.mRailMgr.GetRailLine(r, no);
	this.mTrainOrg[0].SetTopRail = railLine;
	this.mTrainOrg[0].SetRailPos = setRailPos;
	if (num13 > 0)
	{
		int num30 = int.Parse(this.ReadTbl(array[num13])[1]);
		this.mTrainOrg[0].SetDir(num30);
		if (num30 > 0)
		{
			SingletonMonoBehaviour<cGameMgr>.Instance.mSceneMgr.GetSceneCamList(0).RainDirTree.localRotation = Quaternion.identity;
		}
		else
		{
			SingletonMonoBehaviour<cGameMgr>.Instance.mSceneMgr.GetSceneCamList(0).RainDirTree.localRotation = Quaternion.Euler(0f, 180f, 0f);
		}
	}
	this.mTrainOrg[0].InitPos();
	float add = float.Parse(array4[1]);
	float add2 = float.Parse(array4[2]);
	this.mTrainOrg[0].mBtlTrain.SetAdd(add, 0f);
	this.mTrainOrg[0].mBtlTrain.SetAddPer(add2, 0.1f);
	if (num15 > 1)
	{
		r = int.Parse(array3[1]);
		no = int.Parse(array3[2]);
		setRailPos = float.Parse(array3[3]);
		railLine = this.mRailMgr.GetRailLine(r, no);
		this.mTrainOrg[1].SetTopRail = railLine;
		this.mTrainOrg[1].SetRailPos = setRailPos;
		if (num14 > 0)
		{
			int num31 = int.Parse(this.ReadTbl(array[num14])[1]);
			this.mTrainOrg[0].SetDir(num31);
			if (num31 > 0)
			{
				SingletonMonoBehaviour<cGameMgr>.Instance.mSceneMgr.GetSceneCamList(1).RainDirTree.localRotation = Quaternion.identity;
			}
			else
			{
				SingletonMonoBehaviour<cGameMgr>.Instance.mSceneMgr.GetSceneCamList(1).RainDirTree.localRotation = Quaternion.Euler(0f, 180f, 0f);
			}
		}
		this.mTrainOrg[1].InitPos();
		add = float.Parse(array5[1]);
		add2 = float.Parse(array5[2]);
		this.mTrainOrg[1].mBtlTrain.SetAdd(add, 0f);
		this.mTrainOrg[1].mBtlTrain.SetAddPer(add2, 0.1f);
	}
	if (array6 != null)
	{
		int cpu = int.Parse(array6[1]);
		this.mControll.mCPURoot.mCPUTrain.mBtlTrain.m_CPUProc.m_CPU = (Define.eCPU)cpu;
		for (int num32 = 0; num32 < array7.Length - 2; num32++)
		{
			if (num32 < this.mControll.mCPURoot.mCPUTrain.mBtlTrain.m_CPUProc.param.Length)
			{
				this.mControll.mCPURoot.mCPUTrain.mBtlTrain.m_CPUProc.param[num32] = float.Parse(array7[num32 + 2]);
			}
		}
	}
	int num33 = int.Parse(array8[1]);
	if (num33 > 0)
	{
		bool findFlag = true;
		for (int i2 = 0; i2 < this.mComicMgr.ComicList.Count; i2++)
		{
			if (this.mComicMgr.ComicList[i2].sc.ScriptNo == num33)
			{
				findFlag = true;
				string file_name2 = "comic" + num33.ToString("D4") + ".bin";
				byte[] comic_array2 = null;
				for (int i3 = 0; i3 < this.mComicMgr.ComicData_AssetList.Count; i3++)
				{
					string comic_path3 = this.mComicMgr.ComicData_AssetList[i3] + "/" + file_name2;
					string text2 = SingletonMonoBehaviour<cGameMgr>.Instance.Loader.FileChk_Ver(comic_path3);
					if (text2 != null)
					{
						Debug.Log("Find Comic! " + text2);
						comic_array2 = SingletonMonoBehaviour<cGameMgr>.Instance.Loader.LoadByte_Direct(text2);
						break;
					}
					string comic_path4 = SingletonMonoBehaviour<cGameMgr>.Instance.DataPath + this.mComicMgr.ComicData_AssetList[i3] + "/" + file_name2;
					if (File.Exists(comic_path4))
					{
						Debug.Log("Find Comic! " + comic_path4);
						comic_array2 = SingletonMonoBehaviour<cGameMgr>.Instance.Loader.LoadByte_Direct(comic_path4);
						break;
					}
				}
				if (comic_array2 != null && this.mComicMgr.ReReadComic(i2, num33, file_name2, comic_array2))
				{
					Debug.Log("Read Success! " + this.mComicMgr.ComicList[i2].sc.ScriptNo);
					this.mComicMgr.ComicList[i2].sc.IsLoad = true;
					this.mComicMgr.ComicList[i2].StartScript();
					break;
				}
				Debug.Log("Not Found! " + num33);
			}
		}
		if (!findFlag)
		{
			Debug.Log("Not in List! " + num33);
		}
	}
	if (array9 != null)
	{
		int num34 = int.Parse(array9[1]);
		for (int num35 = 0; num35 < this.mComicMgr.mScriptEngine.mCpuCheckerMgr.mEventCheckerList.Count; num35++)
		{
			if (this.mComicMgr.mScriptEngine.mCpuCheckerMgr.mEventCheckerList[num35].Index == num34)
			{
				this.mComicMgr.mScriptEngine.mCpuCheckerMgr.mEventCheckerList[num35].ChkStart();
			}
			else
			{
				this.mComicMgr.mScriptEngine.mCpuCheckerMgr.mEventCheckerList[num35].gameObject.SetActive(false);
			}
		}
	}
	if (array10 != null)
	{
		this.rain_no = int.Parse(array10[1]);
		for (int num36 = 0; num36 < this.mComicMgr.mScriptEngine.mRainCheckerMgr.mEventCheckerList.Count; num36++)
		{
			if (this.mComicMgr.mScriptEngine.mRainCheckerMgr.mEventCheckerList[num36].mScriptLine != null && this.mComicMgr.mScriptEngine.mRainCheckerMgr.mEventCheckerList[num36].mScriptLine.sc.ScriptNo == this.rain_no)
			{
				this.mComicMgr.mScriptEngine.mRainCheckerMgr.mEventCheckerList[num36].ChkStart();
			}
			else
			{
				this.mComicMgr.mScriptEngine.mRainCheckerMgr.mEventCheckerList[num36].gameObject.SetActive(false);
			}
		}
	}
}