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
	int num16 = -1;
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
		else if (array[i].Contains("StageRes:"))
		{
			num11 = i;
		}
		else if (array[i].Contains("SetTexInfo:"))
		{
			num16 = i;
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
		int stageResCnt = int.Parse(this.ReadTbl(array[num11])[1]);
		if (stageResCnt == SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.StageResDataList.Length)
		{
			try
			{
				for (int num41 = 0; num41 < SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.StageResDataList.Length; num41++)
				{
					int num42 = 1;
					string[] array32 = this.ReadTbl(array[num11 + 1 + num41]);
					StageResData stageResData = SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.StageResDataList[num41];
					stageResData.ab = array32[num42++];
					stageResData.res_name = array32[num42++];
				}
			}
			catch (System.Exception ex)
			{
				Debug.LogError("StageRes 読込エラー");
				Debug.LogError(ex.ToString());
			}
		}
	}

	if (num16 > 0)
	{
		int texInfoCnt = int.Parse(this.ReadTbl(array[num16])[1]);
		if (texInfoCnt == SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList.Length)
		{
			int num43 = 0;
			try
			{
				for (int num44 = 0; num44 < SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList.Length; num44++)
				{
					num43 = num44;
					int num45 = 1;
					string[] array33 = this.ReadTbl(array[num16 + 1 + num44]);
					TexInfoData texInfoData = SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[num44];
					texInfoData.amb = int.Parse(array33[num45++]);
					texInfoData.amb_child = int.Parse(array33[num45++]);
					texInfoData.res_data_index = int.Parse(array33[num45++]);
					texInfoData.tex_type = int.Parse(array33[num45++]);
					texInfoData.change_index = int.Parse(array33[num45++]);
					texInfoData.mat_index = int.Parse(array33[num45++]);
					if (texInfoData.tex_type == 31 && array33.Length > num45)
					{
						texInfoData.f1 = float.Parse(array33[num45++]);
						texInfoData.f2 = float.Parse(array33[num45++]);
					}
				}
			}
			catch (System.Exception ex)
			{
				Debug.LogError("TexInfoTex " + num43.ToString() + "番目index 読込エラー");
				Debug.LogError(ex.ToString());
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

			// this.LoadStageTex()
			SingletonMonoBehaviour<MaterialMgr>.Instance.TexNullRemove();
			if (SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.StageResDataList != null)
			{
				for (int i = 0; i < SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.StageResDataList.Length; i++)
				{
					SingletonMonoBehaviour<MaterialMgr>.Instance.AddAssetBundle(SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.StageResDataList[i].ab);
				}
				for (int j = 0; j < SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.StageResDataList.Length; j++)
				{
					this.mAmbMgr.TexList.Add(SingletonMonoBehaviour<MaterialMgr>.Instance.LoadTex(SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.StageResDataList[j].res_name, FilterMode.Bilinear, TextureWrapMode.Repeat, true));
				}
			}

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

	if (num11 > 0 || num16 > 0)
	{
		// this.SetKoukoku()
		for (int i = 0; i < this.mAmbMgr.AmbList.Count; i++)
		{
			try
			{
				if (this.mAmbMgr.AmbList[i].mKoukoku != null)
				{
					for (int j = 0; j < this.mAmbMgr.AmbList[i].mKoukoku.Length; j++)
					{
						if (this.mAmbMgr.AmbList[i].mKoukoku[j] != null && this.mAmbMgr.AmbList[i].mKoukoku[j].Mesh != null && this.mAmbMgr.AmbList[i].mKoukoku[j].Mesh.materials != null && this.mAmbMgr.AmbList[i].mKoukoku[j].Mesh.materials.Length > this.mAmbMgr.AmbList[i].mKoukoku[j].MatIndex)
						{
							Material[] materials = this.mAmbMgr.AmbList[i].mKoukoku[j].Mesh.materials;
							Texture2D texture2D = null;
							if (this.mAmbMgr.AmbList[i].mKoukoku[j].KoukokuType == Define.eKoukoku.e2x1)
							{
								texture2D = this.mRailMgr.mKoukoku2x1.GetRandTex();
							}
							else if (this.mAmbMgr.AmbList[i].mKoukoku[j].KoukokuType == Define.eKoukoku.e1x1)
							{
								texture2D = this.mRailMgr.mKoukoku1x1.GetRandTex();
							}
							else if (this.mAmbMgr.AmbList[i].mKoukoku[j].KoukokuType == Define.eKoukoku.e1x2)
							{
								texture2D = this.mRailMgr.mKoukoku1x2.GetRandTex();
							}
							materials[this.mAmbMgr.AmbList[i].mKoukoku[j].MatIndex].SetTexture(Define.Shader_MainTex, texture2D);
							materials[this.mAmbMgr.AmbList[i].mKoukoku[j].MatIndex].SetTexture(Define.Shader_EmissionMap, texture2D);
							this.mAmbMgr.AmbList[i].mKoukoku[j].Mesh.materials = materials;
						}
					}
				}
			}
			catch (Exception ex)
			{
				if (this.mAmbMgr.AmbList[i].ParentRail != null)
				{
					Debug.LogError(string.Concat(new object[]
					{
						ex.Message,
						i.ToString(),
						" ",
						this.mAmbMgr.AmbList[i].ParentRail.RailIndex
					}));
				}
				else
				{
					Debug.LogError(ex.Message + i.ToString() + " NoParent");
				}
			}
		}

		// this.SetTex()
		if (SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList != null)
		{
			for (int i = 0; i < SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList.Length; i++)
			{
				if (SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].amb >= 0)
				{
					AmbObj ambObj = this.mAmbMgr.Search(SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].amb, SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].amb_child - 1);
					if (ambObj != null)
					{
						if (SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].tex_type == 0 || SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].tex_type == 2)
						{
							Ekihyo ekihyo = ambObj.GetEkihyo(SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].change_index);
							if (ekihyo != null)
							{
								ekihyo.ChangeBord(SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].tex_type, this.mAmbMgr.TexList[SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].res_data_index], SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].mat_index);
							}
						}
						else if (SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].tex_type == 1)
						{
							Ekihyo ekihyo2 = ambObj.GetEkihyo(SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].change_index);
							if (ekihyo2 != null)
							{
								ekihyo2.ChangeBord(SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].tex_type, this.mAmbMgr.TexList[SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].res_data_index], SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].mat_index);
							}
						}
						else if (SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].tex_type == 20)
						{
							HomeNo home = ambObj.GetHome(SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].change_index);
							if (home != null)
							{
								home.ChangeHomeMat(this.mAmbMgr.TexList[SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].res_data_index], SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].mat_index);
							}
						}
						else if (SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].tex_type == 30)
						{
							CngTexUV texUV = ambObj.GetTexUV(SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].change_index);
							if (texUV != null)
							{
								texUV.ChangeTex(this.mAmbMgr.TexList[SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].res_data_index], SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].mat_index);
							}
						}
						else if (SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].tex_type == 31)
						{
							CngTexUV texUV2 = ambObj.GetTexUV(SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].change_index);
							if (texUV2 != null)
							{
								texUV2.ChangeUV(new Vector2(SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].f1, SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].f2), SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].mat_index);
							}
						}
						else if (SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].tex_type == 32)
						{
							CngTexUV texUV3 = ambObj.GetTexUV(SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].change_index);
							if (texUV3 != null)
							{
								texUV3.ChangeActive(SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.TexInfoDataList[i].res_data_index);
							}
						}
					}
					else
					{
						Debug.LogError("NoAmb!! " + i.ToString());
					}
				}
			}
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
			this.mTrainOrg[1].SetDir(num31);
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